#1/usr/bin/python
def compass(commands, available_actions, player, room):
    if len(commands) < 2:
        print "\tUsage: compass [on/off]"
        return


    if commands[1] == "on":
        player.compass = True
        print "\tCompass is on"


    elif commands[1] == "off":
        player.compass = False
        print "\tCompass is off"

    else:

        print "\tUsage: compass [on/off]"


