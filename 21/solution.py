

def get_nbrs(place):
    global map
    x = place[0]
    y = place[1]
    nbrs = []

    # top: y-1
    if y-1 >= 0:
        if map[y-1][x] != "#":
            nbrs.append((x,y-1))

    # bottom: y+1
    if y+1< len(map):
        if map[y+1][x] != "#":
            nbrs.append((x,y+1))

    # left: x-1
    if x-1 >= 0:
        if map[y][x-1] != "#":
            nbrs.append((x-1,y))

    # right: x+1
    if x+1 < len(map[y]):
        if map[y][x+1] != "#":
            nbrs.append((x+1,y))

    return nbrs 


map = []
start = None
with open("puzzle_input.txt", "r") as inp:
#with open("/home/mshaneck/development/advent_of_code/advent_of_code_2023/21/test_input.txt", "r") as inp:
    y = 0
    for line in inp:
        line = line.strip()
        spots = list(line)
        for x in range(len(line)):
            if line[x] == "S":
                start = (x,y)
        map.append(list(line.replace("S",".")))
        y += 1

print("Start: " + str(start))
steps = 64
places = []
places.append({start})
for i in range(steps):
    new_places = set()
    for place in places[i]:
        nbrs = get_nbrs(place)
        for nbr in nbrs:
            new_places.add(nbr,)
    places.append(new_places)

print(len(places[-1]))