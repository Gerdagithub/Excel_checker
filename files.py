# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 20:11:15 2024

@author: gerda
"""

import os

from constants import *

def get_files_from_dir(path):
    directory = os.path.join(CURRENT_PATH, path)
    
    return ([f for f in os.listdir(directory) 
             if os.path.isfile(os.path.join(directory, f))])
