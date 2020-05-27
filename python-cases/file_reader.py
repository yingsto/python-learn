import sys
import os

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
    if len(sys.argv) < 2:
        print("usage: \npython file_reader.py file_name type(optional)")
        exit(0)
    file_name = sys.argv[1]
    type = "txt"
    if len(sys.argv) >= 3:
        type = sys.argv[2]

    if type == "txt":
        txt_reader(file_name)
    elif type == "bin":
        bin_reader(file_name)
    else:
        print("not support file type: %s" %type)
