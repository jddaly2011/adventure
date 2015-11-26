import cmd
import world, tiles, items
from player import Player
from helpa import helpa
#from action_parse import action_parser
from action_parser import action_parser

from parse_translate import parse_translate # natural languiage to game speak

def describe_room(room):

    print room.room_name()
    print room.intro_text()
    if room.inventory:
        for item in room.inventory:
            print "\t{} is here.".format(item.name)

    if room.npcs:
        for npc in room.npcs:
            print "\t{} is here.".format(npc.name)

    room.default(player)
    if room.npcs:
        for npc in room.npcs:
            npc.default(player)

    room.exits_text(player)         
    


def play():
    world.load_tiles()
    global player
    player = Player()
    global room
    room = world.tile_exists(player.location_x, player.location_y)
   
    describe_room(room)

    
    # print room.room_name()
    # print room.intro_text()
    # if room.inventory is not None:
    #     for item in room.inventory:
    #         print "\t{} is here.".format(item.name)

    # if room.npcs is not None:
    #     for npc in room.npcs:
    #         print "\t{} is here.".format(npc.name)

    # room.exits_text(player)         

    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        loc = [player.location_x, player.location_y]
#        describe_room(room)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            global available_actions
            available_actions = room.available_actions()
        
            if player.moves > 0:
                room.default(player)
                if room.npcs:
                    for npc in room.npcs:
                        npc.default(player)


            # print room.room_name()
            # print room.intro_text()
            # if room.inventory is not None:
            #     for item in room.inventory:
            #         print "\t{} is here.".format(item.name)
            #         room.exits_text(player)         
    
            Prompt().cmdloop()

class Prompt(cmd.Cmd):
    """Simple command processor example."""


    prompt = '\t> '
    def default(self, line):
        action_input = parse_translate(line)
        if action_input != "ERROR":
            action_parser(action_input, available_actions, player, room)
        return line

    def do_help(self, tmp="tmp"):# cmd _do_help func takes two arguments so faking it in order to override and call helpa()
        helpa()


if __name__ == "__main__":
    play()
