from heapq import heappush, heappop

map = []
gScore = {}
fScore = {}
cameFrom = {}
with open("puzzle_input.txt", "r") as inp:
#with open("/home/mshaneck/development/advent_of_code/advent_of_code_2023/17/test_input.txt", "r") as inp:
    for line in inp:
        line = line.strip()
        map.append([int(x) for x in line])

start = (0,0)
end = (len(map)-1, len(map[0])-1)

# Heuristic function. Should never overestimate
def h(node):
    global end
    return (end[0]-node[0])+(end[1]-node[1])

def neighbors(node):
    nbrs = []
    # normally, this would be left, right, top and bottom neighbors
    # but let's only add those if the previous three aren't in a straight line - it can move at most 3 in a row
    # also add in that you can't go back where you came from. i.e. if you come from the left, don't consider the left nbr

    # So for part 2, there is a minimum of 4 in a straight line and a maximum of 10
    # However, it is also a minimum of 4 before it can stop, meaning that it can't get to the end node unless it 
    # has gone 4 in a line.
    # so the neighbors have to take that into account
    # and the gScore too
    x = node[0]
    y = node[1]
    dir = node[2]
    repeat = node[3]

    if dir == "":
        # start node, just add the two neighbors
        nbrs.append((x+4,y,">",4))
        nbrs.append((x,y+4,"v",4))

    if dir == ">":
        # we are going right. 
        # consider top and bottom 
        if y-4 >= 0:
            nbrs.append((x,y-4,"^", 4))
        if y+4 < len(map):
            nbrs.append((x,y+4,"v", 4))
        # consider the right neighbor
            # should not have to consider repeat < 4, since we are starting it at 4
        if repeat < 10 and x+1 < len(map[0]):
            nbrs.append((x+1,y, ">", repeat+1))

    if dir == "<":
        # we are going left. 
        # consider top and bottom 
        if y-4 >= 0:
            nbrs.append((x,y-4,"^", 4))
        if y+4 < len(map):
            nbrs.append((x,y+4,"v", 4))
        
        # consider the left neighbor
        if repeat < 10 and x-1 >= 0:
            nbrs.append((x-1,y, "<", repeat+1))

    if dir == "^":
        # we are going up. 
        # consider left and right 
        if x-4 >= 0:
            nbrs.append((x-4,y,"<", 4))
        if x+4 < len(map[0]):
            nbrs.append((x+4,y,">", 4))
        
        # consider the top neighbor
        if repeat < 10  and y-1 >= 0:
            nbrs.append((x,y-1, "^", repeat+1))

    if dir == "v":
        # we are going down. 
        # consider left and right 
        if x-4 >= 0:
            nbrs.append((x-4,y,"<", 4))
        if x+4 < len(map[0]):
            nbrs.append((x+4,y,">", 4))
        
        # consider the bottom neighbor
        if repeat < 10 and y+1 < len(map):
            nbrs.append((x,y+1, "v", repeat+1))

    return nbrs

def d(fromNode, toNode):
    # look in map, but there could be a jump
    # though the jump should be in a straight line
    gs = 0

    # this should work for both adjacents and jumps
    if fromNode[0] == toNode[0]:
        # x is the same, go for y
        inc = 1
        if toNode[1] < fromNode[1]:
            inc = -1
        for y in range(fromNode[1]+inc, toNode[1]+inc, inc):
            gs += map[y][toNode[0]]
    elif fromNode[1] == toNode[1]:
        # y is the same, go for x
        inc = 1
        if toNode[0] < fromNode[0]:
            inc = -1
        for x in range(fromNode[0]+inc, toNode[0]+inc, inc):
            gs += map[toNode[1]][x]
    return gs

def reconstruct_path(node):
    print("Found the answer. This should be the thing that displays it")
    min_node = None
    x = node[0]
    y = node[1]
    for g in gScore:
        if g[0] == x and g[1] == y:
            gs = gScore[g]
            if min_node is None or gs < gScore[min_node]:
                min_node = g
    current_node = min_node
    path = [current_node]
    while current_node in cameFrom:
        current_node = cameFrom[current_node]
        path.insert(0, current_node)

    print(path)
    print(gScore[min_node])
    exit()

gScore[(0,0,"",0)] = 0
fScore[(0,0,"",0)] = h((0,0,"",0))
openset = []
heappush(openset, (0, 0, 0, "", 0))

while len(openset) != 0:
    current_f = heappop(openset)
    current = current_f[1:]
    if current[0] == end[0] and current[1] == end[1]:
        reconstruct_path(current)

    nbrs = neighbors(current)
    for neighbor in nbrs:
        # d(current,neighbor) is the weight of the edge from current to neighbor
        # tentative_gScore is the distance from start to the neighbor through current
        # Need to track in here that the weight is infinite (or not actually a neighbor) if the current stright path length is 3
        # alternatively, I can build this into the neighbor function, to look to see where its come from
        tentative_gScore = gScore[current] + d(current, neighbor)
        if neighbor not in gScore or tentative_gScore < gScore[neighbor]:
            # This path to neighbor is better than any previous one. Record it!
            gScore[neighbor] = tentative_gScore
            fScore[neighbor] = tentative_gScore + h(neighbor)
            cameFrom[neighbor] = current
            # check if neighbor is in openset
            nbr_in_set = False
            for e in openset:
                # check x,y and also dir and repeat
                if e[1] == neighbor[0] and e[2] == neighbor[1] and e[3] == neighbor[2] and e[4] == neighbor[3]:
                    nbr_in_set = True
            if not nbr_in_set:
                heappush(openset, (fScore[neighbor], neighbor[0], neighbor[1], neighbor[2], neighbor[3]))

# Open set is empty but goal was never reached
print("Failed to find path to " + str(end))