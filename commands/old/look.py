#1/usr/bin/python
from examine import examine
def look(commands, available_actions, player, room):
    if len(commands) > 1:
        examine(commands, available_actions, player, room)
    else:
        print "\t{}".format(room.intro_text())
        room.intro_text()
        if room.inventory:
            for item in room.inventory:
                print "\t{} is here.".format(item.name)
        room.exits_text()      
        if room.npcs:
            for npc in room.npcs:
                print "\t{} is here.".format(npc.name)
    
# if __name__ == "__main__":
#     trip()
