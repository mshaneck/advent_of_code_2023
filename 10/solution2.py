
map = []
startX = -1
startY = -1
count = 0

def get_next_location(x,y,fromX,fromY):
    #print("(" + str(x) +"," + str(y) + ")")
    #print("From (" + str(fromX) + "," + str(fromY) + ")")
    # we are traveling to x,y from fromX,fromY. return the coord of the next location
    loc = map[y][x]
    if loc == "|":
        # fromX,fromY should be either above or below
        if fromY == y-1: # above
            return (x,y+1)
        elif fromY == y+1: # below
            return (x,y-1)
    
    if loc == "-": # either left or right
        if fromX == x-1: # left
            return (x+1, y)
        elif fromX == x+1: # right
            return (x-1, y)
        
    if loc == "L": # either right or above
        if fromX == x+1: #right
            return (x,y-1)
        elif fromY == y-1: #above
            return(x+1,y)
    
    if loc == "J": # either left or above
        if fromX == x-1: # left
            return (x,y-1)
        elif fromY == y-1: # above
            return (x-1,y)

    if loc == "7": # either left or below
        if fromX == x-1: # left
            return (x,y+1)
        elif fromY == y+1: # below
            return (x-1,y)
    
    if loc == "F": # either right or below
        if fromX == x+1: # right
            return (x,y+1)
        elif fromY == y+1: # below
            return (x+1,y)

    print("Invalid location combination")
    exit()


cleaned_map = []

with open("puzzle_input.txt", "r") as inp:
    for line in inp:
        cleaned_map.append(['.']*len(line))
        map.append(line)
        if "S" in line:
            startY = count
            startX = line.index("S")
        count += 1

print("Starting coords: (" + str(startX) + ", " + str(startY) + ")")

# travel from the start in both directions until the locations meet up, keeping track of distance

# first get both starting locations at distance 1 from start
top_nbr = (startX, startY-1)
right_nbr = (startX+1, startY)
bottom_nbr = (startX, startY+1)
left_nbr = (startX-1, startY)

starta = None

try:
    if map[top_nbr[1]][top_nbr[0]] == "|" or map[top_nbr[1]][top_nbr[0]] == "7" or map[top_nbr[1]][top_nbr[0]] == "F":
        starta = top_nbr
except:
    pass

try:
    if map[right_nbr[1]][right_nbr[0]] == "-" or map[right_nbr[1]][right_nbr[0]] == "7" or map[right_nbr[1]][right_nbr[0]] == "J":
        if starta is None:
            starta = right_nbr
except:
    pass

try:
    if map[bottom_nbr[1]][bottom_nbr[0]] == "|" or map[bottom_nbr[1]][bottom_nbr[0]] == "L" or map[bottom_nbr[1]][bottom_nbr[0]] == "J":
        if starta is None:
            starta = bottom_nbr
except:
    pass

try:
    if map[left_nbr[1]][left_nbr[0]] == "-" or map[left_nbr[1]][left_nbr[0]] == "F" or map[left_nbr[1]][left_nbr[0]] == "L":
        if starta is None:
            starta = left_nbr
except:
    pass

print(starta)
preva_x = startX
preva_y = startY

a_x = starta[0]
a_y = starta[1]

print(startX)
print(startY)
print(a_x)
print(a_y)

cleaned_map[startY][startX] = "x"
cleaned_map[a_y][a_x] = "x"

steps = 1
while a_x != startX or a_y != startY:
    #print(a_x)
    #print(a_y)
    # Move A
    temp_x = a_x
    temp_y = a_y
    (a_x,a_y) = get_next_location(a_x,a_y,preva_x,preva_y)
    cleaned_map[a_y][a_x] = map[a_y][a_x]
    preva_x = temp_x
    preva_y = temp_y

    #print("A path next step: (" + str(a_x) + "," + str(a_y) + ")" )
    #print("B path next step: (" + str(b_x) + "," + str(b_y) + ")" )

    steps += 1

#for line in cleaned_map:
#    print("".join(line))

inside_count = 0
for i in range(len(cleaned_map)):
    outside = True
    onLine_fromtop = False
    onLine_frombottom = False
    for j in range(len(line)):
        spot = cleaned_map[i][j]
        if spot == "|":
            outside = not outside
        if spot == "F":
            onLine_frombottom = True
        if spot == "L":
            onLine_fromtop = True
        if spot == "J":
            if onLine_frombottom:
                outside = not outside
            onLine_frombottom = False
            onLine_fromtop = False
        if spot == "7":
            if onLine_fromtop:
                outside = not outside
            onLine_frombottom = False
            onLine_fromtop = False

        if spot == "." and outside:
            cleaned_map[i][j] = "O"
        if spot == "." and not outside:
            cleaned_map[i][j] = "I"
            inside_count += 1


for line in cleaned_map:
    print("".join(line))

print(inside_count)
'''
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.'''