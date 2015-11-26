#1/usr/bin/python
def look(commands, available_actions, player, room):
    print "\t{}".format(room.intro_text())
    room.intro_text()
    if room.inventory is not None:
        for item in room.inventory:
            print "\t{} is here.".format(item.name)
        room.exits_text()      

    
# if __name__ == "__main__":
#     trip()
