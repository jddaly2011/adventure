#1/usr/bin/python
import tiles, world

def wear(commands, available_actions, player, room):
    if len(commands) < 2:
        print "\tUsage: wear [item]"
        return
    else:
        if player.inventory is None and room.inventory is None:
            print "\tThere is nothing to wear!"
            return


    with open("things", "r") as f:
        things = f.read()
        f.close()
        things = things.split("\n")
        things = filter(None, things)

        
    if commands[1] not in things:
        print "\tYou cannot take the {}, if there is even really a {} here.".format(commands[1], commands[1])
        return

    items =[]

    for item in room.inventory:
        for sname in item.shortnames:
            items.append(sname)

    for item in player.inventory:
        for sname in item.shortnames:
            items.append(sname)

    if commands[1] not in items:
        print "\tYou cannot see a {} here!".format(commands[1])
        return

    


    for item in room.inventory:
        for sname in item.shortnames:
            if commands[1] == sname:
                if hasattr(item, "wearable"):
                    if not item.worn:
                        print "\tOK, wearing {}.".format(commands[1])
                        room.inventory.remove(item)
                        player.inventory.append(item)
                        item.worn=True
                        player.badged=True
#                        room.mydefault(player)
                        room.available_actions()
                        room.exits_text()
#                        print room.intro_text()
                        return
                    else:
                        print "\tYou are already wearing the {}.".format(commands[1])
            else:
                print "\tYou cannot wear the {}.".format(commands[1])
                return
    

    for item in player.inventory:
        for sname in item.shortnames:
            if commands[1] == sname:
                if hasattr(item, "wearable"):
                    print "\tOK, wearing {}.".format(commands[1])
                    player.badged= True
                    item.worn=True
#                    room.mydefault(player)
                    room.available_actions()
                    room.exits_text()
#                    print room.intro_text()
                    return
                else:
                    print "\tYou cannot wear the {}.".format(commands[1])





        # wearing = False
        # for item in player.inventory:
        #     if commands[1] in item.shortnames:
        #         wearing = True
        #         player.badged= True
         #         print '\tOK, wearing badge'

#                 room.mydefault(player)
#                 room.available_actions()
#                 room.exits_text()
#                 print room.intro_text()

#         if not wearing:
#             print "\tYou do not have the {}.".format(commands[1])

#     else:
#          print "\tYou cannnot wear the {}.".format(commands[1])

# # 
    #     if __name__ == "__main_":
#     trip()
