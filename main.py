import openpyxl
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet
import os
import logging

from constants import *
from custom_logging import *
from excel import *
from files import *

                
setup_logging(True)

answers_wb = get_workbook(os.path.join(ANSWERS_PATH, ANSWER_FILE))    
solutions_wbs = get_files_from_dir(SOLUTIONS_PATH)
check_solutions_of_wb(answers_wb, solutions_wbs)

print("Done")
