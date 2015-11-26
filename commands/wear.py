#1/usr/bin/python
import tiles, world
from get_item import get_item 

def wear(commands, available_actions, player, room):
    if len(commands) < 2:
        print "\tUsage: wear [item]"
        return
    else:
        if player.inventory is None and room.inventory is None:
            print "\tThere is nothing to wear!"
            return

    item, owner = get_item(room, player, commands[1])# owner = room, player, openable, npc, npc_item

    if not item:

        things = owner

        if commands[1] not in things:
            print "\tI do not know the word {}.".format(commands[1])
            return

        if commands[1] in things:
            print "\tYou don't see the {} here.".format(commands[1])
            return

    if owner == "room":
        if hasattr(item, "wearable"):
            print "\tOK, wearing {}.".format(commands[1])
            room.inventory.remove(item)
            player.inventory.append(item)
            item.worn=True
            player.badged=True
            room.default(player)
            available_actions = room.available_actions()
            room.exits_text(player)
            return


    if owner == "player":
        if hasattr(item, "wearable"):
            if not item.worn:
                print "\tOK, wearing {}.".format(commands[1])
                item.worn=True
                player.badged=True
                room.default(player)
                available_actions = room.available_actions()
                room.exits_text(player)
                return
            else:
                print "\tYou are already wearing the {}.".format(commands[1])
    else:
        print "\tYou cannot wear the {}.".format(commands[1])
        return


    


#     for item in room.inventory:
#         for sname in item.shortnames:
#             if commands[1] == sname:
#                 if hasattr(item, "wearable"):
#                     if not item.worn:
#                         print "\tOK, wearing {}.".format(commands[1])
#                         room.inventory.remove(item)
#                         player.inventory.append(item)
#                         item.worn=True
#                         player.badged=True
# #                        room.mydefault(player)
#                         room.available_actions()
#                         room.exits_text(player)
# #                        print room.intro_text()
#                         return
#                     else:
#                         print "\tYou are already wearing the {}.".format(commands[1])
#             else:
#                 print "\tYou cannot wear the {}.".format(commands[1])
#                 return
    

#     for item in player.inventory:
#         for sname in item.shortnames:
#             if commands[1] == sname:
#                 if hasattr(item, "wearable"):
#                     print "\tOK, wearing {}.".format(commands[1])
#                     player.badged= True
#                     item.worn=True
# #                    room.mydefault(player)
#                     room.available_actions()
#                     room.exits_text(player)
# #                    print room.intro_text()
#                     return
#                 else:
#                     print "\tYou cannot wear the {}.".format(commands[1])





        # wearing = False
        # for item in player.inventory:
        #     if commands[1] in item.shortnames:
        #         wearing = True
        #         player.badged= True
         #         print '\tOK, wearing badge'

#                 room.mydefault(player)
#                 room.available_actions()
#                 room.exits_text(player)
#                 print room.intro_text()

#         if not wearing:
#             print "\tYou do not have the {}.".format(commands[1])

#     else:
#          print "\tYou cannnot wear the {}.".format(commands[1])

# # 
    #     if __name__ == "__main_":
#     trip()


