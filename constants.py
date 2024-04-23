import os

LOG_FILE_NAME = "logs.log"
FILE_LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s:\n%(message)s\n'
CONSOLE_LOG_FORMAT = '%(name)s - %(levelname)s:\n%(message)s\n'
LOG_TYPE_INFO = 'info'
LOG_TYPE_DEBUG = 'debug'
LOG_TYPE_WARNING = 'warining'
LOG_TYPE_ERROR = 'error'

CURRENT_PATH = os.getcwd()
SOLUTIONS_PATH = os.path.join(CURRENT_PATH, "..", "solutions")
ANSWERS_PATH = os.path.join(CURRENT_PATH, "..", "answers")

ANSWER_FILE = '1_10.xlsx'

WORKBOOK_WITH_CALCULATED_VALUES = 'wb_values'
WORKBOOK_WITH_FORMULAS = 'wb_formulas'

SEPARATOR = '------------------------------ NEW FILE -----------------------------------'
MAX_SAME_COLUMN_RESPONSES = 7