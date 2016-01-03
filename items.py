class Item(object):
    """The base class for all items"""
    def __init__(self, name, description, value, shortnames, takeable):
        self.name = name
        self.description = description
        self.value = value
        self.shortnames = shortnames
        self.takeable = takeable

# class Thing(Item):
#     def __init__(self, name, description, value, takeable, openable):
# #        self.shortnames = shortnames
# #        self.takeable=takeable
#         super(Thing, self).__init__(name, description, takeable, openable, shortnames)
        


class Openable(Item):
    def __init__(self, name, description, value, shortnames, takeable, inventory, opened):
        self.inventory = inventory
        self.opened=opened
#        self.takeable=takeable
        super(Openable, self).__init__(name, description, value, shortnames, takeable)




        

class Fridge(Openable):
    def __init__(self):
        super(Fridge, self).__init__(name="A refrigerator",
                                   description="\tIt's the refrigerator in the breakroom. There is a sign on it that says \n\t 'Do Not Steal Food. Honor System Strictly Enforced'.",
                                   value=10, 
                                   shortnames=['fridge', 'refrigerator', 'icebox'],
                                   takeable=False,
#                                   inventory=["lunch", "coffee"],
                                   inventory=[Sandwich()],
                                   opened=False
                                   )


class Readable(Item):
    def __init__(self, name, description, value, shortnames, takeable, read):
        self.read=read
#        self.takeable=takeable
        super(Readable, self).__init__(name, description, value, shortnames, takeable)


class Map(Readable):
    def __init__(self):
        super(Map, self).__init__(name="A map",
                                   description="\tIt's the floorplan of the office. Zeros seems to indicate walls.",
                                   value=10, 
                                   shortnames=['map', 'floorplan', 'blueprint'],
                                   takeable=True,
                                   read=False
                                   )

    def display(self):
        with open("newmap.txt", "r") as f:
            mymap = f.read()
            f.close()
            mymap = mymap.split("\n")
            mymap = filter(None, mymap)

        for line in mymap:
            print line

class Schedule(Readable):
    def __init__(self):
        super(Schedule, self).__init__(name="A schedule",
                                   description="\tIt seems to be the office scheduel for the day", 
                                   value=10, 
                                   shortnames=['schedule', 'sked'],
                                   takeable=True,
                                   read=False
                                   )

    def display(self):
        with open("sked.txt", "r") as f:
            myschedule = f.read()
            f.close()
            myschedule = myschedule.split("\n")
            myschedule = filter(None, myschedule)

        print "The schedule reads:\n\n"

        for line in myschedule:
            print line
        

class Clipboard(Readable):
    def __init__(self):
        super(Clipboard, self).__init__(name="A clipboard",
                                   description="\tAn official looking clipboard, the kind that make you appear to be really getting things done.",
                                   value=10, 
                                   shortnames=['clipboard'],
                                  takeable=True,
                                   read=False)

    def display(self):
        with open("clipboard.txt", "r") as f:
            clipboard = f.read()
            f.close()
            clipboard = clipboard.split("\n")
            clipboard = filter(None, clipboard)

        for line in clipboard:
            print line








class Wearable(Item):
    def __init__(self, name, description, value, shortnames, takeable, wearable, worn):
        self.wearable=wearable
        self.worn=worn
        super(Wearable, self).__init__(name, description, value, shortnames, takeable)


class id_badge(Wearable):
    def __init__(self):
        super(id_badge, self).__init__(name="An ID badge",
                                   description="\tAn ID Badge that says 'Larry Melman'",
                                   value=10, 
                                   shortnames=['id', 'badge'],
                                     takeable=True,
                                     wearable=True,
                                      worn=False
)

class Food(Item):
    def __init__(self, name, description, value, shortnames, takeable, eatable, eaten):
        self.eatable=eatable
        super(Food, self).__init__(name, description, value, shortnames, takeable)


class Sandwich(Food):
    def __init__(self):
        super(Sandwich, self).__init__(name="a sandwich",
                                   description="\tIt is a sandwich lunch that has 'Bob' written on the wrapper",
                                   value=10, 
                                   shortnames=['sandwich'],
                                     takeable=True,
                                    eatable=True,
                                    eaten=False
)

class Cake(Food):
    def __init__(self):
        super(Cake, self).__init__(name="A birthday cake",
                                   description="\tIt's a bithday cake that says \n\t 'happy goddam birthday larry are you happy now?'",
                                   value=10, 
                                   shortnames=['cake'],
                                   takeable=True,
                                    eatable=True,
                                    eaten=False

 
)

class Pen(Item):
    def __init__(self):
        super(Pen, self).__init__(name="A pen",
                                   description="\tIt's a sweet pen that has 4 different colored inks.",
                                   value=10, 
                                   shortnames=['pen','biro'],
                                  takeable=True


)





 
class USB(Item):
    def __init__(self):
        super(USB, self).__init__(name="A USB stick",
                                   description="\tIt's a USB stick in the shape of a slice of pizza.",
                                   value=10, 
                                   shortnames=['usb', 'usbstick', 'stick'],
                                   takeable=True

)

















# class Weapon(Item):
#     def __init__(self, name, description, value, damage):
#         self.damage = damage
#         super(Weapon, self).__init__(name, description, value)

#     def __str__(self):
#         return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


# class Rock(Weapon):
#     def __init__(self):
#         super(Rock, self).__init__(name="Rock",
#                          description="A fist-sized rock, suitable for bludgeoning.",
#                          value=0,
#                          damage=5)


# class Dagger(Weapon):
#     def __init__(self):
#         super(Dagger,self).__init__(name="Dagger",
#                          description="A small dagger with some rust. Somewhat more dangerous than a rock.",
#                          value=10,
#                          damage=10)


# class Gold(Item):
#     def __init__(self, amt):
#         self.amt = amt
#         super(Gold, self).__init__(name="Gold",
#                          description="A round coin with {} stamped on the front.".format(str(self.amt)),
#                          value=self.amt)
