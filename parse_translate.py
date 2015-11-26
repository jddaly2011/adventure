#!/usr/bin/python
import os
import re
import sys
def parse_translate(action_input):
   action_input = action_input.strip()
   action_input = action_input.lower()
   
   if action_input == "l":
      action_input="look"
   if action_input == "q" or action_input == 'exit':
      action_input="quit"

   if action_input == "i":
      action_input="inventory"


   if action_input == "help":
      action_input="helpa"

   
#   print "input is |{}|".format(action_input)
   action_input = re.sub("  ", " ", action_input)
   if action_input == "":
      action_input = "?"
      print "\tExcuse me?"
   if action_input == "quit":
      sys.exit()



   action_input = re.sub("^$", " ", action_input)
   action_input = re.sub("^move ", "", action_input)
   action_input = re.sub("north", "n", action_input)
   action_input = re.sub("south", "s", action_input)
   action_input = re.sub("east", "e", action_input)
   action_input = re.sub("west", "w", action_input)
   action_input = re.sub("put on", "wear", action_input)   
   
   thesaurus  = {}
   with open("thesaurus") as f:
      for line in f:
         (key, val) = line.split(":")
         thesaurus[key] = val

   words = action_input.split()
   changed = False
   for idx, word in enumerate(words):
      if word in thesaurus:
         changed = True
         words[idx]= thesaurus[word]
    
   if changed:
      action_input =""
      for x in range(len(words)):
         action_input = action_input + " " + words[x]

      action_input = action_input.lstrip()


   
   # tmp_commands = (os.listdir("commands/"))
   # valid_commands =[]
   # for command in tmp_commands:
   #    newcommand = re.sub("\.pyc", "", command)
   #    newcommand = re.sub("\.py", "", newcommand)
   #    newcommand = re.sub("helpa", "help", newcommand)
   #    if newcommand != "__init__" and  newcommand != "skel":
   #       valid_commands.append(newcommand)
      
   # valid_commands = set(valid_commands)
   # print valid_commands
 

   # with open("commands", "r") as f:
   #   valid_commands = f.read()
   #   f.close()
   #   valid_commands = valid_commands.split("\n")
   #   valid_commands = filter(None, valid_commands)


   # commands = action_input.split()
   # if commands[0] not in valid_commands:
   #    print "\tI do not understand {}".format(action_input)
   #    return "ERROR"


   
   return action_input
