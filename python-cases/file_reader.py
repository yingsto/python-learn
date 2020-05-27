import sys
import os
import argparse

def txt_reader(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            print("line: %s" %line)

# encoding: utf-8, gbk, gb18030,
# errors = "ignore"
# bytes <-> string: bytes.hex() -> string, bytes.fromhex(string) -> bytes
# hexdump -C -v xxx.bin
def bin_reader(file_name):
    with open(file_name, "rb") as f:
        data = f.read()
        string = data.hex()

    with open("bin_string.dat", "w") as f:
        f.write(string)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--file_name", dest="name", help="file name", type=str)
    parser.add_argument("-t", "--file_type", default='txt', dest="type", help="file type", type=str)
    args = parser.parse_args()
    if len(sys.argv) < 3:
        print("usage: \npython file_reader.py -n file_name -t file_type")
        exit(0)
    file_name = args.name
    type = args.type
    if type == "txt":
        txt_reader(file_name)
    elif type == "bin":
        bin_reader(file_name)
    else:
        print("not support file type: %s" %type)
