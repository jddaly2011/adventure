#!/usr/bin/python
import actions, world, items, npcs, player

#player.inventory = []
#player.compass = True
class MapTile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.inventory =[]
        self.ordinary =[]
        self.npcs= []
        self.moves = -1
#        self.name = name
#        self.default(player)
    def default(self, player):
#        raise NotImplementedError()
        self.moves += 1
#        print "Moves:{}".format(self.moves)

    def intro_text(self):
        raise NotImplementedError()

    def room_name(self):
        raise NotImplementedError()

    def list_items(self):
        for item in self.inventory:
            print item

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
#        myroom = world.tile_exists(self.x, self.y)
    
        if world.tile_exists(self.x + 1, self.y):

           moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
           # myroom= world.tile_exists(self.x + 1, self.y)
           # if type(myroom).__name__ == LockedNorth:
           #     pass
           # else:
           #     moves.append(actions.MoveNorth())

        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        
        # myroom = world.tile_exists(self.x, self.y)
        # if isinstance(myroom, LockedDoorRoom):
        #      print "door is locked"
        #      print myroom.door

        if isinstance(self, LockedDoorRoom) and not self.solved:
             for move in moves:
                if isinstance(move, actions.MoveNorth) and self.door == "north":
                    moves.remove(move)
                if isinstance(move, actions.MoveSouth) and self.door == "south":
                    moves.remove(move)
                if isinstance(move, actions.MoveEast) and self.door == "east":
                    moves.remove(move)
                if isinstance(move, actions.MoveWest) and self.door == "west":
                    moves.remove(move)
        

#        print moves
        return moves

    

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
#        moves.append(actions.DescribeItem())
#        moves.append(actions.DescribeAnItem(item=item))

        return moves

    def draw_compass(self, exits):

        if "north" in exits:
            print u"""
                                N
                                |"""

        else:
            print "\n"

        if "west" in exits and "east" in exits:
            print u"""
                            W  \u2014*\u2014  E"""
        elif "west" in exits:
            print u"""
                            W  \u2014*"""

        elif "east" in exits:
            print u"""
                                *\u2014  E"""

        else:
            print u"""
                                *"""

        if "south" in exits:
            print"""
                                |
                                S
"""


    def exits_text(self, player):
        """Returns all move actions for adjacent tiles."""
        exits = []
        if world.tile_exists(self.x + 1, self.y):
            exits.append("east")
        if world.tile_exists(self.x - 1, self.y):
            exits.append("west")
        if world.tile_exists(self.x, self.y - 1):
            exits.append("north")
        if world.tile_exists(self.x, self.y + 1):
            exits.append("south")

        # need to check if LockedRoom so we can lock appropiate door
        #myroom = world.tile_exists(self.x, self.y)
        if isinstance(self,LockedDoorRoom) and not self.solved:
             door = self.door
             exits.remove(door)




        if len(exits) == 1:
            print "\tThere is an exit to the {}".format(exits[0])
        elif len(exits) == 2:
            print "\tThere are exits to the {} and {}".format(exits[0], exits[1])
        elif len(exits) == 3:
            print "\tThere are exits to the {}, {}, and {}".format(exits[0], exits[1], exits[2])
        elif len(exits) == 4:
            print "\tThere are exits to the {}, {}, {}, and {}".format(exits[0], exits[1], exits[2], exits[3])
        else:
            if isinstance(self, Elevator):
                print "\tThe elevator door is closed"
                         
            else:
                print "\tThere appears to be no way out"

        if player.compass:
            # print "\n"
            # if "north" in exits:
            #     print "\t\t\tN"
            #     print "\n\n"

            # if "east" in exits and "west" in exits:
            #     print "\tW\t\t\t\tE"
            #     print "\n\n"

            # elif "west" in exits:
            #     print "\tW"
            #     print "\n\n"

            # elif "east" in exits:
            #     print "\t\t\t\t\tE"
            #     print "\n\n"
            # else:
            #     print "\n\n"

            # if "south" in exits:
            #     print "\t\t\tS"
            self.draw_compass(exits)
            
# class NPCoom(MapTile):
#     def __init__(self, x, y, npcs):
#         self.npcs = npcs
#         super(NPCRoom, self).__init__(x, y)


class CFOOffice(MapTile):
    def __init__(self, x, y):
        super(CFOOffice,self).__init__(x, y)
        self.inventory = [items.USB(), items.Map()]
        self.name = "CFOOffice"
    def intro_text(self):
        return """
        You are in a a CFO's office.
        """

    def modify_player(self, player):
        #Room has no action on player
        pass
 
    def room_name(self):
        return "\t\tThe CFO's office"


class CEOOffice(MapTile):
    def __init__(self, x, y):
        super(CEOOffice,self).__init__(x, y)
#        self.inventory = []
        self.npcs =  [npcs.CEO(self.x, self.y)]
        self.name = "CEOOffice"
        
    def intro_text(self):
        return """
        You are in a a CEO's office.
        """

    def modify_player(self, player):
        #Room has no action on player
        pass
 
    def room_name(self):
        return "\t\tThe CEO's office"

class LockedDoorRoom(MapTile):
    def __init__(self, x, y):
        super(LockedDoorRoom, self).__init__(x, y)
        self.door = ""
    def return_exits(self):
        raise NotImplementedError()
        

class Reception(LockedDoorRoom):
    def __init__(self, x, y):
        super(Reception, self).__init__(x, y)
        self.name = "Reception"

        self.solved = False 
        self.door = "north"
        self.inventory = [items.Map()]
#        self.npcs= []
        self.npcs =  [npcs.Receptionist(self.x, self.y)]

#        print self.moves

    def default(self, player):
#        print vars(items.id_badge())
#        if player.badged:
        self.moves += 1
        for item in player.inventory:
            for sname in item.shortnames:
                if sname == "id":
                    if item.worn:
                        self.solved = True
                        available_actions = self.available_actions()
                        return
                else:
                    self.solved = False
                    
                                            

    def intro_text(self):
        if self.solved:
            return """
        You are at Reception.
        There is a receptionist here 
        """
        else:
            return """
        You are at Reception.
        There is a receptionist here.
        There is locked door to the  north.
        """

            
    def modify_player(self, player):
        #Room has no action on player
        pass

    def room_name(self):
        return "\t\tReception"


class HallwayLocked(LockedDoorRoom):
    def __init__(self, x, y):
        super(HallwayLocked, self).__init__(x, y)
        self.name = "HallwayLocked"
        self.solved = False 
        self.door = "south"
#        print self.moves

    def default(self, player):
        self.moves += 1

        for item in player.inventory:
            for sname in item.shortnames:
                if sname == "id":
                    if item.worn:
                        self.solved = True
#                        global available_actions
                        available_actions = self.available_actions()
                        return
                else:
                    self.solved = False


                        
    def intro_text(self):
        # for item in player.inventory:
        #     if hasattr(item, "worn") and item.worn:
        #         self.solved = True
        if self.solved:
            return """
        You are in a  Hallway.
        """
        else:
            return """
        You are in a Hallway.
        There is locked door to the south.
        """

            
    def modify_player(self, player):
        #Room has no action on player
        pass

    def room_name(self):
        return "\t\tHallway"






class Elevator(LockedDoorRoom):
    def __init__(self, x, y):
        super(Elevator,self).__init__(x, y)
        self.inventory = [items.id_badge()]
        self.ordinary = ['screen']
        self.solved = False 
        self.door = "north"
        self.name = "Elevator"

    #self.inventory = [items.cake()]

    def intro_text(self):
        if not self.solved:
            return " "
        else:    
            return """
        You are in an elevator. There is a button and a keyhole.
        """


    def modify_player(self, player):
        #Room has no action on player
        pass

    def room_name(self):
        return "\t\tElevator"

    def default(self, player):
        self.moves += 1
        if not self.solved:
            if self.moves == 0:
                print "\tYou are in an elevator. The elevator is ascending. You notice a screen on the wall. It says 'Type \"compass off\" to turn the compass off'"

            if self.moves == 1:
                print "\tThe elevator is ascending. The screen now says 'Advertise here. 65% of NPCs read this screen'"

            if self.moves == 2:
                self.solved = True
                print "\tThe elevator comes to a stop and the door opens.You may exit to the north."
    #            print self.solved
                moves = self.available_actions()
           #     self.exits_text()

#        self.moves = self.moves +1


class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You find yourself if a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

    def room_name(self):
        return "\t\tStarting Room"


class Kitchen(MapTile):
    def __init__(self, x, y):
        super(Kitchen,self).__init__(x, y)
        self.inventory = [items.Fridge()]
        self.name = "Kitchen"
        self.npcs =  [npcs.CFO(self.x, self.y)]

    def intro_text(self):
        return """
        You are in a wee kitchen
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
 
    def room_name(self):
        return "\t\tSmall Kitchen"


class ConfRoomNorth(MapTile):
    def __init__(self, x, y):
        super(ConfRoomNorth,self).__init__(x, y)
        self.inventory = [items.Cake()]
        self.ordinary=['whiteboard','board']
        self.name = "ConfRoomNorth"

    def intro_text(self):
        return """
        You are in a conference room. The lights flicker eerily. There is a whiteboard kere.
        You wonder how do paragraphs display.
        """

    def modify_player(self, player):
        #Room has no action on player
        pass

    def room_name(self):
        return "\t\tConference Room North"




class ConfRoomNorth1(MapTile):
    def __init__(self, x, y):
        super(ConfRoomNorth1,self).__init__(x, y)
        self.name = "ConfRoomNorth1"

    def intro_text(self):
        return """
        A conference room. the lights are flickering and there is a case of water bottles here
        """

 
    def modify_player(self, player):
        #Room has no action on player
        pass

    def room_name(self):
        return "\t\tConference Room North 1"


class ConfRoomNorth2(MapTile):
    def __init__(self, x, y):
        self.name = "ConfRoomNorth2"

    def intro_text(self):
        return """
        An unremarkable conference room. There is a man on a screen looking at you.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

    def room_name(self):
        return "\t\tConference Romm North 2"
    
class ConfRoom(MapTile):
    def __init__(self, x, y):
        super(ConfRoom,self).__init__(x, y)

        self.name= "ConfRoom"
    
    def intro_text(self):
        return """
        You are in another goddamn conference room
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

    def room_name(self):
        return "\t\tConference Room"
        

class Room(MapTile):
    def __init__(self, x, y):
        super(Room,self).__init__(x, y)

        self.name = "Room"
    def intro_text(self):
        return """
        You are in a room. A hideous room. 
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

    def room_name(self):
        return "\t\tRoom"""

class OfficeManagerOffice(MapTile):
    def __init__(self, x, y):
        super(OfficeManagerOffice,self).__init__(x, y)
        
        self.name = "OfficeManagerOffice"
    def intro_text(self):
        return """
        You are in the office manager's office.
        """

 
    def modify_player(self, player):
        #Room has no action on player
        pass

    def room_name(self):
        return "\t\tOffice Manager's office"

class StorageCloset(MapTile):
    def __init__(self, x, y):
        super(StorageCloset, self).__init__(x, y)

        self.name = "StorageCloset"
    def intro_text(self):
        return """
        You are in a storage closet. There are stores here
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

    def room_name(self):
        return "\t\tStorage Closet"

class Hallway(MapTile):
    def __init__(self, x, y):
        super(Hallway,self).__init__(x, y)
        self.name = "Hallway"
    def intro_text(self):
        return """
        You are in an empty beige hallway. You feel empty inside.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
 
    def room_name(self):
        return "\t\tHallway"


class CIOOffice(MapTile):
    def __init__(self, x, y):
        super(CIOOffice,self).__init__(x, y)
        self.npcs =  [npcs.CIO(self.x, self.y)]

        self.name = "CIOOffice"
    def intro_text(self):
        return """
        You are in the CIO's office
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

    def room_name(self):
        return "\t\tCIO's office"
 
    def default(self, player):
        self.moves += 1

class CopierRoom(MapTile):
    def __init__(self, x, y):
        super(CopierRoom,self).__init__(x, y)

        self.name = "CopierRoom"
    def intro_text(self):
        return """
        You are in a copier room.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
    def room_name(self):
        return "\t\tCopier Room"

class MensBathroom(MapTile):
    def __init__(self, x, y):
        super(MensBathroom, self).__init__(x, y)

        self.name = "MensBathroom"
    def intro_text(self):
        return """
        You are in a filthy mens room
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

    def room_name(self):
        return "\t\tMens Bathroom"

class MensStall(MapTile):
    def __init__(self, x, y):
        super(MensStall,self).__init__(x, y)

        self.name = "MensStall"
    def intro_text(self):
        return """
        You are in a bathroom stall. There is graffiti on the walls.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
 
    def room_name(self):
        return "\t\tBathroom Stall"


class MensUrinal(MapTile):
    def __init__(self, x, y):
        super(MensUrinal,self).__init__(x, y)

        self.name = "MensUrinal"

    def intro_text(self):
        return """
        This is a men's unrinal.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
    def room_name(self):
        return "\t\tMens Urinal"
