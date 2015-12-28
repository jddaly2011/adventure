global _world
_world = {}
# global starting_position
# starting_position = (0, 0)
 
def load_tiles():
    print "loading world..."
    """Parses a file that describes the world space into the _world object"""
    with open('newmap.txt', 'r') as f:
        rows = f.readlines()
        x_max = len(rows[0].split()) # Assumes all rows contain the same number of tabs
        for y in range(len(rows)):
            cols = rows[y].split()
            for x in range(x_max):
                tile_name = cols[x].replace('\n', '') # Windows users may need to replace '\r\n'
                if not tile_name:
                    print "NO TILE NAME"
                # print x, y
                # print tile_name
                if tile_name == 'Elevator':
                    #print "StartingRoom Found"
                    global starting_position
                    starting_position = (x, y)
                    
                _world[(x, y)] =  None if tile_name == '0' else getattr(__import__('tiles'), tile_name)(x, y)
                # print _world[(x,y)]
                # print "added"
        
def tile_exists(x, y):
    # try: 
    #     print x,y, _world[(x,y)].room_name
    # except:
    #     print x, y
    # if _world[(x,y)] is not None:
    #     print _world[(x,y,)].room_name
#    print type(_world.get((x, y)))
    return _world.get((x, y))

def allrooms():
    xtemp = []
    ytemp = []
    for x, y in _world:
        xtemp.append(x)
        ytemp.append(y)
    temp = zip(xtemp, ytemp)
    return temp


def mapref():
    refmap = {}
    for x, y in _world:
        ref = (x, y)
        tmproom = tile_exists(x, y)
        if tmproom:
            refmap[tmproom.name] = ref
    return refmap


