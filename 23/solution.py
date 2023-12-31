import sys
sys.setrecursionlimit(5000)

max_length = 0

def get_nbrs(prev, current):
    global maze
    # check the four cardinal directions
    x = current[0]
    y = current[1]
    p_x = prev[0]
    p_y = prev[1]
    nbrs = []

    if maze[y][x] == ">":
        if (x+1,y) != prev:
            nbrs.append((x+1,y))
        return nbrs
    if maze[y][x] == "<":
        if (x-1,y) != prev:
            nbrs.append((x-1,y))
        return nbrs
    if maze[y][x] == "^":
        if (x,y-1) != prev:
            nbrs.append((x,y-1))
        return nbrs
    if maze[y][x] == "v":
        if (x,y+1) != prev:
            nbrs.append((x,y+1))
        return nbrs

    # top: y-1
    if y-1 >= 0:
        if y-1 != p_y:
            if maze[y-1][x] != "#" and maze[y-1][x] != "v":
                nbrs.append((x,y-1))

    # bottom: y+1
    if y+1< len(maze):
        if y+1 != p_y:
            if maze[y+1][x] != "#" and maze[y+1][x] != "^":
                nbrs.append((x,y+1))

    # left: x-1
    if x-1 >= 0:
        if x-1 != p_x:
            if maze[y][x-1] != "#" and maze[y][x-1] != ">":
                nbrs.append((x-1,y))

    # right: x+1
    if x+1 < len(maze[y]):
        if x+1 != p_x:
            if maze[y][x+1] != "#" and maze[y][x+1] != "<":
                nbrs.append((x+1,y))

    return nbrs 

def find_path(prev, current, end, current_length):
    global max_length
    # look for neighbors
    # mostly there will be one, not counting where it came from
    if current == end:
        print("Found a path of length " + str(current_length))
        if current_length > max_length:
            max_length = current_length
        return 
    
    nbrs = get_nbrs(prev, current)
    # iterate without recursion while possible. i.e. obly recurse for a branch
    while len(nbrs) == 1:
        nbr = nbrs[0]
        current_length += 1
        if nbr == end:
            print("Found a path of length " + str(current_length))
            if current_length > max_length:
                max_length = current_length
            return 

        prev = current
        current = nbr
        nbrs = get_nbrs(prev, current)


    if len(nbrs) > 1:
        #print("Found a branch at " + str(current))
        #print(nbrs)
        for nbr in nbrs:
            find_path(current, nbr, end, current_length+1)

maze = []
with open("puzzle_input.txt", "r") as inp:
#with open("/home/mshaneck/development/advent_of_code/advent_of_code_2023/23/test_input.txt", "r") as inp:
    for line in inp:
        line = line.strip()
        maze.append(line)

start = (-1,0)
end = (-1,-1)

for x in range(len(maze[0])):
    if maze[0][x] == ".":
        start = (x,0)

for x in range(len(maze[len(maze)-1])):
    if maze[len(maze)-1][x] == ".":
        end = (x,len(maze)-1)

print("Going from " + str(start) + " to " + str(end))
    
find_path((-1,-1), start, end, 0)

print("Max length path: " + str(max_length))