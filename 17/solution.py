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
def h(x,y):
    global end
    return (end[0]-x)+(end[1]-y)

def neighbors(x,y, dir, repeat):
    nbrs = []
    # normally, this would be left, right, top and bottom neighbors
    # but let's only add those if the previous three aren't in a straight line - it can move at most 3 in a row
    # also add in that you can't go back where you came from. i.e. if you come from the left, don't consider the left nbr
    if x > 0:
        # we can consider the left neighbor
        nbr_x = x-1
        nbr_y = y
        nbr_dir = "<"
        if dir == nbr_dir and repeat< 3:
            nbrs.append((nbr_x, nbr_y, nbr_dir, repeat+1))
        elif dir != nbr_dir and dir != ">":
            nbrs.append((nbr_x, nbr_y, nbr_dir, 1))

    if x < len(map[0])-1:
        # we can consider the right neighbor
        nbr_x = x+1
        nbr_y = y
        nbr_dir = ">"
        if dir == nbr_dir and repeat< 3:
            nbrs.append((nbr_x, nbr_y, nbr_dir, repeat+1))
        elif dir != nbr_dir and dir != "<":
            nbrs.append((nbr_x, nbr_y, nbr_dir, 1))
        
    if y > 0:
        # we can consider the top neighbor
        nbr_x = x
        nbr_y = y-1
        nbr_dir = "^"
        if dir == nbr_dir and repeat< 3:
            nbrs.append((nbr_x, nbr_y, nbr_dir, repeat+1))
        elif dir != nbr_dir and dir != "v":
            nbrs.append((nbr_x, nbr_y, nbr_dir, 1))

    if y < len(map)-1:
        # we can consider the bottom neighbor
        nbr_x = x
        nbr_y = y+1
        nbr_dir = "v"
        if dir == nbr_dir and repeat< 3:
            nbrs.append((nbr_x, nbr_y, nbr_dir, repeat+1))
        elif dir != nbr_dir and dir != "^":
            nbrs.append((nbr_x, nbr_y, nbr_dir, 1))
        
    return nbrs

def reconstruct_path(x, y):
    print("Found the answer. This should be the thing that displays it")
    min_node = None
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
fScore[(0,0,"",0)] = h(0,0)
4+1+1+5
openset = []
heappush(openset, (0, 0, 0, "", 0))

while len(openset) != 0:
    (current_f, current_x, current_y, current_dir, current_rep) = heappop(openset)
    if current_x == end[0] and current_y == end[1]:
        reconstruct_path(current_x, current_y)

    nbrs = neighbors(current_x, current_y, current_dir, current_rep)
    for neighbor in nbrs:
        # d(current,neighbor) is the weight of the edge from current to neighbor
        # tentative_gScore is the distance from start to the neighbor through current
        # Need to track in here that the weight is infinite (or not actually a neighbor) if the current stright path length is 3
        # alternatively, I can build this into the neighbor function, to look to see where its come from
        tentative_gScore = gScore[(current_x, current_y, current_dir, current_rep)] + map[neighbor[1]][neighbor[0]]
        if neighbor not in gScore or tentative_gScore < gScore[neighbor]:
            # This path to neighbor is better than any previous one. Record it!
            gScore[neighbor] = tentative_gScore
            fScore[neighbor] = tentative_gScore + h(neighbor[0], neighbor[1])
            cameFrom[neighbor] = (current_x, current_y, current_dir, current_rep)
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