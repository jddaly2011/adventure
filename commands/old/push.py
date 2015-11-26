#1/usr/bin/python
def push(commands, available_actions, player, room):
    if len(commands) < 2:
        print "\tUsage: push [something]"
        return

    with open("pushables", "r") as f:
        pushables = f.read()
        f.close()
        pushables = pushables.split("\n")
        pushables = filter(None, pushables)


    if commands[1] in pushables:
        if commands[1] == "button":
            for item in player.inventory:
                if "key" in item.shortnames:
                    print "success"
                else:
                    print "\tPushing the button has no effect. Perhaps a key is needed"
    else:
        print "\tPushing the {} has no effect.".format(commands[1])



    
# if __name__ == "__main__":
#     trip()
