import cmd
import world, tiles, items
from player import Player
#from helpa import helpa
import os
import re
import datetime

def add_move(player, room):
    player.moves+= 1
    player.add_time()
#     room.default(player)
#     if hasattr(room, "npcs"):
#         for npc in room.npcs:
#             npc.default(player)
#    print "\tMoves: {}".format(player.moves)
    # print "\t{}".format(room.room_name()),
    # mytime = player.time.strftime("%H:%M")
    # print mytime
def loadImports(path):
    files = os.listdir(path)
    imps = []

    for i in range(len(files)):
        name = files[i].split('.')
        if len(name) > 1:
            if name[1] == 'py' and name[0] != '__init__':
               name = name[0]
               imps.append(name)

    file = open(path+'__init__.py','w')

    toWrite = '__all__ = '+str(imps)

    file.write(toWrite)
    file.close()

loadImports("commands/")
from commands import *

def action_parser(action_input, available_actions, player, room):

   directions = ['n','s','e','w']
   valid = []
   available_actions = room.available_actions()
   for action in available_actions:
      valid.append(action.hotkey)
#      print action.hotkey
#   print "\n\n"
   if action_input in directions:
      if action_input in valid:
         for action in available_actions:
            if action_input == action.hotkey:
                player.do_action(action, **action.kwargs)
                add_move(player, room)
               
                return
      else:
         print "\tYou walk into a wall."
         add_move(player, room)
         return

   else:

       tmp_commands = (os.listdir("commands/"))
       valid_commands =[]
       for command in tmp_commands:
           newcommand = re.sub("\.pyc", "", command)
           newcommand = re.sub("\.py", "", newcommand)
           newcommand = re.sub("helpa", "help", newcommand)
           if newcommand != "__init__" and  newcommand != "skel":
               valid_commands.append(newcommand)
               
       valid_commands = set(valid_commands)

       commands = action_input.split()
       if commands[0] not in valid_commands:
           print "\tI do not understand {}".format(action_input)
#           add_move(player)
           return "ERROR"
       else:
           func = "{}.{}(commands, available_actions, player, room)".format(commands[0], commands[0])
           exec func                     
           add_move(player, room)
           print "\n"

