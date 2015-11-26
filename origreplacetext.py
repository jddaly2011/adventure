#!/usr/bin/python

import os
import re
import sys

argnum = len(sys.argv)

if argnum < 4:
    print "Usage: oldtext newtest file"
    sys.exit(1)



oldtext = sys.argv[1]
newtext = sys.argv[2]
#mypath = "/path/to/files"
#mypath = "/home/pi/bin/tmpd/"
# oldtext = "currfile"
# newtext = "replaced text"

for x in range(3, argnum):
    filename = sys.argv[x]
    if os.path.isdir(filename) != True:
        f = open(filename, "r")
        currfile = f.read()
        f.close()
        newfile =[]
        currfile = currfile.split("\n")
        if any(oldtext in s for s in currfile):
            for line in currfile:
                line = re.sub(oldtext, newtext, line)
                newfile.append(line)
                f = open(filename, "w")
                for line in newfile:
                    f.write(line)
                    f.write("\n")
            f.close()



