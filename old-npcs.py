import actions, world, items, player, tiles

class NPC:
    def __init__(self, name, shortnames, description, inventory):
        self.name = name
        self.shortnames = shortnames
        self.description = description
        self.inventory = inventory
        self.ordinary =[]
        self.moves = 0
    
    def default(self, player):
        pass

    def describe_npc(self):
        print self.description

class CFO(NPC):
    def __init__(self):
        NPC.__init__(
            self, 
            name="The CFO", 
            shortnames = ['CFO','cfo'],
            description = "\tThe CFO appears to be a large white rabbit wearing a top hat and waistcoat.",
            inventory=[items.Clipboard()])

    def default(self, player):
        self.moves += 1
        # print self.moves
        # if self.moves == 1:
        #     print "hello"
    


class CEO(NPC):
    def __init__(self):
        NPC.__init__(
            self, 
            name="The CEO", 
            shortnames = ['CEO','ceo'],
            description = "\tThe CEO strongly resembles Richard Branson, especially the smell.",
            inventory=[])

    def default(self, player):
        self.moves += 1


class Receptionist(NPC):
    def __init__(self):
        NPC.__init__(
            self, 
            name="The receptionist", 
            shortnames = ['receptionist','branislav', 'bran'],
            description = "\tThe receptionist is Branislav, a former champion weightlifter.",
            inventory=[])
    
    def default(self, player):
        self.moves += 1
        if player.badged:
            print "\tBranislav speaks:"
            print '\t\t"Hello Larry, I am Branislav."'
        else:
            print "\tBranislav speaks:"
            print '\t\t"Doors will not open if you not wearing badge."'

    
