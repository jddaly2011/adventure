import cmd
import world, tiles, items
from player import Player
from helpa import helpa
from schedule import sched
#from action_parse import action_parser
from action_parser import action_parser

from parse_translate import parse_translate # natural languiage to game speak

def describe_room(room):

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
            #npc.default(player)
            pass
    room.exits_text(player)         
    # for x, y in world.allrooms():
    #     print x, y
    #     tmproom= world.tile_exists(x, y)
    #     if tmproom and tmproom.npcs:
    #         for npc in tmproom.npcs:
    #             npc.default(player)


def play():
    world.load_tiles()
    global player
    player = Player()
    global room
    room = world.tile_exists(player.location_x, player.location_y)
    mapref = world.mapref()
    for k in mapref:
        print k
        print mapref[k]
    print type(mapref)

    describe_room(room)

    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        loc = [player.location_x, player.location_y]
#        room.modify_player(player)
        if player.is_alive() and not player.victory:
            global available_actions
            available_actions = room.available_actions()
        
            if player.moves > 0:
#                print "Running all rooms NPC default"
                room.default(player)
                temp = world.allrooms()
                npclist =[]
                for x, y in temp:
                    
                    tmproom= world.tile_exists(x, y)
                    if tmproom and tmproom.npcs:
                        for npc in tmproom.npcs:
                            if npc.name not in npclist: #we haven't called default on npc yet for this move
                                npc.default(player)
                                npclist.append(npc.name)
                                #print "called default on {}".format(npc.name)
        Prompt().cmdloop()

class Prompt(cmd.Cmd):
    """Simple command processor example."""

    prompt = '\t> '
    def default(self, line):
        action_input = parse_translate(line)
        if "schedule" in action_input:
            sched(action_input, available_actions, player, room)
            return
        if action_input != "ERROR":
            action_parser(action_input, available_actions, player, room)
        return line

    def do_help(self, tmp="tmp"):# cmd _do_help func takes two arguments so faking it in order to override and call helpa()
        helpa()


if __name__ == "__main__":
    play()
