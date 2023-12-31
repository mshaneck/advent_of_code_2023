import sys
sys.setrecursionlimit(10000)

max_length = 0

def get_nbrs(current, visited):
    # check the four cardinal directions
    x = current[0]
    y = current[1]
    nbrs = []

    # top: y-1
    if y-1 >= 0:
        if maze[y-1][x] != "#" and (x,y-1) not in visited:
            nbrs.append((x,y-1))

    # bottom: y+1
    if y+1< len(maze):
        if maze[y+1][x] != "#" and (x,y+1) not in visited:
            nbrs.append((x,y+1))

    # left: x-1
    if x-1 >= 0:
        if maze[y][x-1] != "#" and (x-1,y) not in visited:
            nbrs.append((x-1,y))

    # right: x+1
    if x+1 < len(maze[y]):
        if maze[y][x+1] != "#" and (x+1,y) not in visited:
            nbrs.append((x+1,y))

    return nbrs 

def find_path(current, end, current_length, visited):
    global max_length
    # look for neighbors
    # mostly there will be one, not counting where it came from
    if current == end:
        if current_length > max_length:
            print("Found a new longest path of length " + str(current_length))
            max_length = current_length
        return 

    nbrs = get_nbrs(current, visited)
    # iterate without recursion while possible. i.e. obly recurse for a branch
    while len(nbrs) == 1:
        nbr = nbrs[0]
        current_length += 1
        if nbr == end:
            if current_length > max_length:
                print("Found a new longest path of length " + str(current_length))
                max_length = current_length
            return 

        current = nbr
        nbrs = get_nbrs(current, visited)

    if len(nbrs) > 1:
        #print("Found a branch at " + str(current))
        #print(nbrs)
        #random.shuffle(nbrs)
        #print(nbrs)
        visited += (current,)
        for nbr in nbrs:
            find_path(nbr, end, current_length+1, visited)

maze = []
with open("puzzle_input.txt", "r") as inp:
#with open("/home/mshaneck/development/advent_of_code/advent_of_code_2023/23/test_input.txt", "r") as inp:
    for line in inp:
        line = line.strip()
        line = line.replace(">",".").replace("<",".").replace("v",".").replace("^",".")
        maze.append(list(line))

start = (-1,0)
end = (-1,-1)

for x in range(len(maze[0])):
    if maze[0][x] == ".":
        start = (x,0)

for x in range(len(maze[len(maze)-1])):
    if maze[len(maze)-1][x] == ".":
        end = (x,len(maze)-1)

visited = ()

print("Going from " + str(start) + " to " + str(end))
find_path(start, end, 0, visited)
print("Max length path: " + str(max_length))