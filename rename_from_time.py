#!/usr/bin/python3.6
"""
The script renames files of selected type and add numbers
of files to the begin of names
max_count_files = 100
Select type of files in the SETTINGS
"""

import os

# SETTINGS
TYPE_FILES = ".mp4"
# SETTINGS

list_name_all = os.listdir(path=".")
list_name = []
for item in list_name_all:
    if item.find(TYPE_FILES) >= 0:
        list_name.append(item)

if not list_name:
    print("Files of selected type wasn't found")
list_time = []
for item in list_name:
    list_time.append(os.path.getmtime(item))

x = zip(list_name, list_time)
xs = sorted(x, key=lambda tup: tup[1])
list_name_sort = [x[0] for x in xs]


for i, item in enumerate(list_name_sort):
    if len(list_name_sort) < 10:
        re_item = "0{}_{}".format(i+1, item)
        os.replace(item, re_item)
    elif len(list_name_sort) >= 10 and len(list_name_sort) < 100:
        if i <= 8:
            re_item = "00{}_{}".format(i+1, item)
            os.replace(item, re_item)
        elif i >= 9:
            re_item = "0{}_{}".format(i+1, item)
            os.replace(item, re_item)
