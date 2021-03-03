#!/usr/bin/python3.6
"""
The script renames files and directories in the current directory
to the POSIX standart
"""

import os


list_fls = os.listdir(path=".")
list_renamed_fls = []

bad_symbols = "?'\"#$^();<>[]|\\*@~&!,"
whitespace = " "
tab = "\t"


def main():
    for fl in list_fls:
        list_renamed_fl = []
        for bad in bad_symbols:
            if fl.find(bad) >= 0:
                fl = fl.replace(bad, "")
                list_renamed_fl.append(fl)
            elif fl.find(whitespace) >= 0:
                fl = fl.replace(whitespace, "_")
                list_renamed_fl.append(fl)
            elif fl.find(tab) >= 0:
                fl = fl.replace(tab, "_")
                list_renamed_fl.append(fl)
            else:
                list_renamed_fl.append(fl)
        list_renamed_fls.append(list_renamed_fl[-1])
    for i in range(len(list_fls)):
        if list_fls[i] != list_renamed_fls[i]:
            os.replace(list_fls[i], list_renamed_fls[i])
            print("{} ===> {}".format(list_fls[i], list_renamed_fls[i]))


if __name__ == "__main__":
    main()
