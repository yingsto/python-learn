import os
import re
import sys
import argparse


ignore_file = [".git", ".~", ".DS_Store"]

def check_ignore_file(s):
    for file in ignore_file:
        if re.search(file, s):
            return True
    return False


def get_file_list(file_path, s, level):
    if(level == 0):
        if not check_ignore_file(file_path):
            s.append(file_path)
            #print("level = %d: file_path = %s, file_lists = %s" %(level, file_path, s))
        return

    if os.path.isdir(file_path):
        files = os.listdir(file_path)
        for file in files:
            path = file_path + "/" + file
            get_file_list(path, s, int(level-1))
    else:
        if not check_ignore_file(file_path):
            s.append(file_path)
            #print("level = %d: file_path = %s, file_lists = %s" %(level, file_path, s))


def get_type_from_file_list(s, type):
    files = []
    for file in s:
        if file.endswith(type):
            files.append(file)
    return files

def get_file_from_file_list(s, file_name):
    files = []
    for file in s:
        if re.search(file_name, file):
            files.append(file)
    return files


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--file_path", dest="path", help="file path", type=str)
    parser.add_argument("-l", "--level_number", default=-1, dest="level", help="level number", type=int)
    parser.add_argument("-t", "--file_type", default='', dest="type", help="file type", type=str)
    parser.add_argument("-n", "--file_name", default='', dest="name", help="file name", type=str)
    args = parser.parse_args()
    if (len(sys.argv) < 3):
        print("usage: \npython file_explorer.py -f file_path -l level -t type -n name")
        exit(0)
    file_path = args.path
    level = args.level
    type = args.type
    name = args.name
    s = []
    if(os.path.exists(file_path)):
        get_file_list(file_path, s, level)
        with open("file_lists.log","w") as f:
            for file in s:
                f.write(file)
                f.write("\n")

        files = get_type_from_file_list(s, type)
        with open("type_files.log","w") as f:
            for file in files:
                f.write(file)
                f.write("\n")

        files = get_file_from_file_list(s, name)
        with open("name_files.log","w") as f:
            for file in files:
                f.write(file)
                f.write("\n")