import logging
import os

from constants import *

# Setup logging
def setup_logging(rewrite_log_file):
    if (rewrite_log_file and os.path.exists(LOG_FILE_NAME)):
        logger = logging.getLogger()
        for handler in logger.handlers[:]:
            handler.close()
            logger.removeHandler(handler)
            
        os.remove(LOG_FILE_NAME)  
    
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # File handler - logs all messages
    file_handler = logging.FileHandler(LOG_FILE_NAME)
    file_formatter = logging.Formatter(FILE_LOG_FORMAT)
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.DEBUG)

    # Console handler - logs only error messages
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter(CONSOLE_LOG_FORMAT)
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(logging.ERROR)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
'''
log message is a dictionary:
    {
        type: 
        value:
    }
'''
def print_log_message(message):
    if (message is None):
        return
    
    msg_type = message.get('type')
    msg_value = message.get('value')
    if ((msg_type is None) or (msg_value is None)):
        return
    
    if (msg_type == LOG_TYPE_INFO):
        logging.info(msg_value)
        
    elif (msg_type == LOG_TYPE_DEBUG):
        logging.debug(msg_value)
        
    elif (msg_type == LOG_TYPE_WARNING):
        logging.warning(msg_value)
        
    elif (msg_type == LOG_TYPE_ERROR):
        logging.error(msg_value)
        
'''
log message is a dictionary:
    {
        column:
        response:
            {
                type: 
                value:
            }
    }
'''
def log_responses(responses):
    sorted_responses = sorted(responses, key=lambda r: r['column'])

    for response in sorted_responses:
        log_data = response.get('response')
        if not log_data:  # Check if 'response' key exists and has a value
            continue
        
        print_log_message(log_data)
    
    