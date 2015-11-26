import items
import world
import npcs

 
class Player():
    def __init__(self):
        self.inventory = [items.Pen()]
        self.hp = 100
        self.location_x, self.location_y = world.starting_position
        self.victory = False
        self.eaten = []
        self.badged = False
        self.moves = 0
        self.compass = True
    def is_alive(self):
        return self.hp > 0
 
    def print_inventory(self):
        if self.inventory:
            print "\tYou are carrying:"
            for item in self.inventory:
                print"\t{}".format(item.name)

#    def describe_item(self, itemname="A pen"):
    def describe_item(self):
        if self.inventory:
            for item in self.inventory:
                print "\t{}".format(item.name)
                print "\t{}".format(item.description)





    def describe_an_item(self, item):
        if self.inventory:
            if item in self.inventory:
                print "\t{}".format(item.description)

    def describe_npc(self, npc):
        print npcs.npc.description
        # if world(self.location_x, self.location_y) is type(NPCRoom):
        #     print "This is NPC room"



    def move(self, dx, dy):
        last_room = world.tile_exists(self.location_x, self.location_y)
        npcs_to_move =[]

        self.location_x += dx
        self.location_y += dy
#         if last_room.npcs:

# #            print last_room.npcs
#             for npc in reversed(last_room.npcs):
#                 npc.x = self.location_x
#                 npc.y = self.location_y
#                 NPC = 1
#                 print "\t{} follows you.".format(npc.name)
#                 npcs_to_move.append(npc)
#                 last_room.npcs.remove(npc)
#             print "\n\n"
        
#        print self.location_x, self.location_y
        

        #print (world.tile_exists(self.location_x, self.location_y))

        room = world.tile_exists(self.location_x, self.location_y)
        # if npcs_to_move > 0:
        #     for npc in npcs_to_move:
        #         room.npcs.append(npc)

        print room.room_name()

        room.default(self)
        if room.npcs:
            for npc in room.npcs:
                npc.default(self)
        
        print room.intro_text()
        if room.inventory:
             for item in room.inventory:
                 print "\t{} is here.".format(item.name)

        if room.npcs:
            for npc in room.npcs:
                print "\t{} is here.".format(npc.name)


        room.exits_text(self)         

        # print room.room_name()
        # room.default(self)
        # print room.intro_text()
        # if room.inventory is not None:
        #     for item in room.inventory:
        #         print "\t{} is here.".format(item.name)
        # room.exits_text(player)




        # print(world.tile_exists(self.location_x, self.location_y).room_name())
        # print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    # def attack(self, enemy):
    #     best_weapon = None
    #     max_dmg = 0
    #     for i in self.inventory:
    #         if isinstance(i, items.Weapon):
    #             if i.damage > max_dmg:
    #                 max_dmg = i.damage
    #                 best_weapon = i
 
    #                 print("You use {} against {}!".format(best_weapon.name, enemy.name))
    #                 enemy.hp -= best_weapon.damage
    #                 if not enemy.is_alive():
    #                     print("You killed {}!".format(enemy.name))
    #                 else:
    #                     print("{} HP is {}.".format(enemy.name, enemy.hp))

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)
        
