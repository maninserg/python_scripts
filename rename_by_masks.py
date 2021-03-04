#!/usr/bin/python3.6
import os
"""
The script replaces MASK_DEL to MASK_PS in names of files in the current directory
Write MASK_DEL and MASK_PS in SETTINGS
"""


# SETTINGS
MASK_DEL ="_Программирование_на_Python"
MASK_PS = ""
# SETTINGS

list_name_all = os.listdir(path=".")

for item in list_name_all:
    os.replace(item,item.replace(MASK_DEL,MASK_PS))



