#!/usr/bin/python

import os
import re
import sys

argnum = len(sys.argv)

if argnum < 2:
    print "Usage: replacetext.py startingroom"
    sys.exit(1)



oldtext = "if tile_name ==.*:"
newtext = "if tile_name == '{}':".format(sys.argv[1])


for x in range(1, argnum):
    filename = "world.py"
    f = open(filename, "r")
    currfile = f.read()
    f.close()
    newfile =[]
    currfile = currfile.split("\n")

    # if any(oldtext in s for s in currfile):
    #     print found
    #     for line in currfile:
    #         line = re.sub(oldtext, newtext, line)
    #         newfile.append(line)
    #         f = open(filename, "w")
    #         for line in newfile:
    #             f.write(line)
    #             f.write("\n")
    #     f.close()


    for line in currfile:
        line = re.sub(oldtext, newtext, line)
        newfile.append(line)
        f = open(filename, "w")
        for line in newfile:
            f.write(line)
            f.write("\n")
    f.close()



