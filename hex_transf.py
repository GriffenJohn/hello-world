import os
import sys
import re

count = 0

def repl(matched):
    global count
    string = matched.group(0)
    res = string[2:4] + string[0:2] + " " + string[6:8] + string[4:6] + " " + string[10:] + string[8:10] + "\n"
    res = "{0:05d}: ".format(count) + res
    count = count + 1
    return res

file_name = sys.argv[1]
dest_name = sys.argv[2]
fs = open(file_name, "r")
fs_d = open(dest_name, "w")

comm = ""
fs.readline()
while 1:
    line = fs.readline()[9:-3]
    if line == "": break
    comm += line

comm = re.sub(r"(\w\w\w\w){3}", repl, comm)
fs_d.write("       R    G    B\n")
fs_d.write(comm)

fs.close()
fs_d.close()
