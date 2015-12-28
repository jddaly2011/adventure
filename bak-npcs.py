import actions, world, items, player, tiles
class NPC(object):
    def __init__(self, x, y):
        self.x= x
        self.y= y
        self.moves = 0
        self.dest = None
        self.last =[]
        self.nd = {}
    def default(self, player):
        self.moves += 1
        if self.dest:
            print self.shortnames[0]
            print self.x, self.y
            print self.nd
            this_room = world.tile_exists(self.x, self.y)
            print this_room.npcs
            if self.x == self.destx and self.y == self.desty: #we made it
                print "Trip completed {}, {}".format(self.x, self.y)
                self.nd = {}
                self.dest = None
                return
            if self.moves % 2 != 0: #wait two moves before moving
                print "WAITING~~"
                return
            else:
                print "MOVING"
                available_exits = self.exits()
                print "Exits: {}".format(available_exits)
                x, xdir, y, ydir = self.get_dir()
                
                print self.nd
                if len(available_exits) == 1:
                    func = "self.move_{}(this_room, player)".format(available_exits[0])
                    exec func                     
                    return
                
                if xdir and (self.x + x, self.y) not in self.last:
                    if xdir in available_exits:
                        func = "self.move_{}(this_room, player)".format(xdir)
                        exec func                     
                        return

                elif ydir and (self.x, self.y + y) not in self.last:
                    if ydir in available_exits:
                        func = "self.move_{}(this_room, player)".format(ydir)
                        exec func                     
                        return
                
                elif xdir and self.nd[(self.x + x, self.y)] < 2:
                    if xdir in available_exits:
                        func = "self.move_{}(this_room, player)".format(xdir)
                        exec func                     
                        return

                elif ydir:
                    if (self.x, self.y + y) in self.nd:
                        print nd
                        if self.nd[(self.x, self.y + y)] < 2:
                            if ydir in available_exits:
                                func = "self.move_{}(this_room, player)".format(xdir)
                                exec func                     
                                return
                    else:
                        if ydir in available_exits:
                            func = "self.move_{}(this_room, player)".format(xdir)
                            exec func                     
                            return


    def update_nd(self):
        for t in self.last:
            if t not in self.nd:
                self.nd[t] = 1
            else:
                self.nd[t] +=1


    def get_dir(self):
        x = 0
        y = 0
        if self.x < self.destx and world.tile_exists(self.x + 1, self.y):
            print "xdir is east"
            xdir = 'east'
            x = 1
        elif self.x > self.destx and world.tile_exists(self.x - 1, self.y):
            xdir = 'west'
            x = -1
            print "xdir is west"
        else:
            xdir = None
            x = 0
            print "xdir is None"
        if self.y > self.desty and world.tile_exists(self.x, self.y -1):
            ydir = "north"
            y = -1
            print "ydir is north"
        elif self.y <  self.desty and world.tile_exists(self.x, self.y +1):
            print "ydir is south"
            ydir = "south"
            y = 1
        else:
            ydir = None
            print "ydir is None"
            y = 0
        return x, xdir, y, ydir

    def move_east(self, this_room, player):
        print "moving east"
        self.move_npc(this_room, 1, 0, player)

    def move_west(self, this_room, player):
        print "moving west"
        self.move_npc(this_room, -1, 0, player)

    def move_north(self, this_room, player):
        print "moving north"
        self.move_npc(this_room, 0, -1, player)

    def move_south(self, this_room, player):
        print "moving south"
        self.move_npc(this_room, 0, 1, player)

    def move_npc(self, this_room, x, y, player):
        print "x: {} y: {}".format(x, y)
        this_room.npcs.remove(self)
        new_room = world.tile_exists(self.x + x, self.y + y)
        new_room.npcs.append(self)
        print this_room.npcs
        self.last.append((self.x, self.y))
        self.update_nd()
        self.x += x
        self.y += y
        print "new loc {}, {}".format(self.x, self.y)

        if player.location_x == this_room.x and player.location_y == this_room.y:
            if x != 0:
                if x > 0:
                    mydir = "east"
                else:
                    mydir = "west"
            else:
                if y > 0:
                    mydir = "south"
                else:
                    mydir = "north"
                
            print "\t{} leaves the room to the {}.".format(self.name, mydir)
            return
        elif player.location_x == new_room.x and player.location_y == new_room.y:
            print "entering"

            print "\t{} enters the room.".format(self.name)

            return
        return


    def exits(self):
        """Returns all move actions for adjacent tiles."""
        available_exits = []
        if world.tile_exists(self.x + 1, self.y):
            available_exits.append("east")
        
        if world.tile_exists(self.x - 1, self.y):
            available_exits.append("west")
        if world.tile_exists(self.x, self.y - 1):
            available_exits.append("north")
        if world.tile_exists(self.x, self.y + 1):
            available_exits.append("south")

        return available_exits

    def describe_npc(self):
        print self.description

class CFO(NPC):
    def __init__(self, x,y):
        super(CFO ,self).__init__(x, y)
        self.name="The CFO"
        self.shortnames = ['cfo']
        self.description = "\tThe CFO appears to be a large white rabbit wearing a top hat and waistcoat."
        self.inventory=[items.Clipboard()]



class CEO(NPC):
    def __init__(self, x, y):
        super(CEO ,self).__init__(x, y)
        self.name="The CEO"
        self.shortnames = ['CEO','ceo']
        self.description = "\tThe CEO strongly resembles Richard Branson, especially the smell."
        self.inventory=[]


class CIO(NPC):
    def __init__(self, x, y):
        super(CIO ,self).__init__(x, y)
        self.name="The CIO"
        self.shortnames = ['CIO','cio']
        self.description = "\tThe CIO is an Android-American."
        self.inventory=[]



    # def default(self, player):
    #     self.moves += 1


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
#        print "\tRoom moves: {}".format(self.moves)
        if player.badged:
            if not self.intro and player.location_x == self.x and player.location_y == self.y:
                print "\tBranislav speaks:"
                print '\t\t"Hello Larry, I am Branislav."'
                self.intro = True
        elif player.location_x == self.x and player.location_y == self.y:
            print "\tBranislav speaks:"
            print '\t\t"Doors will not open if you not wearing badge."'

        if player.moves % self.moves == 0 and player.location_x == self.x and player.location_y == self.y:
            print "\tConversation goes here"
            print player.moves % self.moves
