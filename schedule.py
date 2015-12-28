#1/usr/bin/python
import world
def sched(commands, available_actions, player, room):
    print type(commands)
    mapref = world.mapref()
    for k in mapref:
        print k
    print mapref[commands[2]]
    if commands[2] not in mapref:
        print "\t{} is not the name of a room.".format(commands[2])
        return
    destx, desty = mapref[commands[2]]
    
    temp = world.allrooms()
    npclist =[]
    for x, y in temp:
        tmproom= world.tile_exists(x, y)
        if tmproom and tmproom.npcs:
            for npc in tmproom.npcs:
#                if npc.shortnames[0] == commands[1]:
                if commands[1] in npc.shortnames:
                    npc.dest = True
                    # npc.destx = mapref[commands[2][0]]
                    # npc.desty = mapref[commands[2][1]]
                    npc.destx = destx
                    npc.desty = desty
                    print "destination {}, {}".format(npc.destx, npc.desty)
                    return
# if __name__ == "__main__":
#     trip()
