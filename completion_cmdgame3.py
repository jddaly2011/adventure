import cmd, os, re
import world, tiles, items
from player import Player
from helpa import helpa
#from action_parse import action_parser
from action_parser import action_parser

from parse_translate import parse_translate # natural languiage to game speak

    


def play():
    world.load_tiles()
    global player
    player = Player()
    global room
    room = world.tile_exists(player.location_x, player.location_y)
    
    

    
    print room.room_name()
    print room.intro_text()
    if room.inventory is not None:
        for item in room.inventory:
            print "\t{} is here.".format(item.name)
    room.exits_text()         
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            global available_actions
            available_actions = room.available_actions()
            # print room.room_name()
            # print room.intro_text()
            # if room.inventory is not None:
            #     for item in room.inventory:
            #         print "\t{} is here.".format(item.name)
            #         room.exits_text()         
    
            Prompt().cmdloop()

class Prompt(cmd.Cmd):
    """Simple command processor example."""
    prompt = '\t> '

    tmp_commands = (os.listdir("commands/"))
    valid_commands =[]
    for command in tmp_commands:
        newcommand = re.sub("\.pyc", "", command)
        newcommand = re.sub("\.py", "", newcommand)
        newcommand = re.sub("helpa", "help", newcommand)
        if newcommand != "__init__" and  newcommand != "skel":
            valid_commands.append(newcommand)

    valid_commands = set(valid_commands)

    def default(self, line):
        self.do_mytest(self, line)
        return line

    def do_mytest(self, line):
        action_input = parse_translate(line)
        if action_input != "ERROR":
            action_parser(action_input, available_actions, player, room)
        return line


    def complete_mytest(self, text, line, begidx, endidx):
        if not text:
            completions = self.valid_commands
            return completions
        else:
            print "completing"
            completions = []
            for f in self.valid_commands:
                if f.startswith(text):
                    completions.append(f)
                           
            return completions

    def do_EOF(self, line):
        return True 
    

            


    def do_help(self, tmp="tmp"):# cmd _do_help func takes two arguments so faking it in order to override and call helpa()
        helpa()
    

if __name__ == "__main__":
    play()
