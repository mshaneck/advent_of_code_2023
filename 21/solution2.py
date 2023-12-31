
def get_nbrs(place):
    global map
    x = place[0]
    y = place[1]
    nbrs = []

    y_max = len(map)
    x_max = len(map[y%y_max])

    #print("Need to add coords for which repeat its on. ")
    # start with  added 0,0. Increase or decrease the respective coord if the 
    # or, we could stick with straight up coordinates and just use % to see what the value is...

    # top: y-1
    if map[(y-1)%y_max][x%x_max] != "#":
        nbrs.append((x,y-1))

    # bottom: y+1
    if map[(y+1)%y_max][x%x_max] != "#":
        nbrs.append((x,y+1))

    # left: x-1
    if map[y%y_max][(x-1)%x_max] != "#":
        nbrs.append((x-1,y))

    # right: x+1
    if map[y%y_max][(x+1)%x_max] != "#":
        nbrs.append((x+1,y))

    return nbrs 


map = []
start = None
#with open("puzzle_input.txt", "r") as inp:
with open("/home/mshaneck/development/advent_of_code/advent_of_code_2023/21/test_input.txt", "r") as inp:
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
steps = 500
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