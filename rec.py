import actions, world, items, player, tiles

class NPC(object):
    def __init__(self, x, y):
        self.x= x
        self.y= y
        self.moves = 0
    
    def default(self, player):
        pass

    def describe_npc(self):
        print self.description

class CFO(NPC):
    def __init__(self, x,y):
        super(CFO ,self).__init__(x, y)
        self.name="The CFO"
        self.shortnames = ['CFO','cfo']
        self.description = "\tThe CFO appears to be a large white rabbit wearing a top hat and waistcoat."
        self.inventory=[items.Clipboard()]

    def default(self, player):
        self.moves += 1
        # print self.moves
        # if self.moves == 1:
        #     print "hello"
    


class CEO(NPC):
    def __init__(self, x, y):
        super(CEO ,self).__init__(x, y)
        self.name="The CEO"
        self.shortnames = ['CEO','ceo']
        self.description = "\tThe CEO strongly resembles Richard Branson, especially the smell."
        self.inventory=[]

    def default(self, player):
        self.moves += 1


class Receptionist(NPC):
    def __init__(self, x, y):
        super(Receptionist ,self).__init__(x, y)
        self.name="The receptionist"
        self.shortnames = ['receptionist','branislav', 'bran']
        self.description = "\tThe receptionist is Branislav, a former champion weightlifter."
        self.inventory=[]
        self.intro=False
    def default(self, player):
        self.moves += 1
        if player.badged:
            if not self.intro:
                print "\tBranislav speaks:"
                print '\t\t"Hello Larry, I am Branislav."'
                self.intro = True
        else:
            print "\tBranislav speaks:"
            print '\t\t"Doors will not open if you not wearing badge."'

        if player.moves % self.moves == 0:
            print "\tConversation goes here"
    
