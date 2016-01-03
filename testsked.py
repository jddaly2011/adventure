#!/usr/bin/python
import datetime
from datetime import timedelta

with open("sked.txt", "r") as f:
    master = f.read()
    f.close()
    # master = master.split("\n")
    # master = filter(None, master)

print master

when, where, who = master.split()

print when
print type(who)
who = who.split(",")
print type(who)
print who
for w in who:
    print w

hour = int(when[0:2])
minute= int(when[2:4])
print hour, minute
#t = datetime.time(hour=hour, minute=minute)
t = datetime.datetime(2015, 6, 1, hour, minute, 0)
print t
