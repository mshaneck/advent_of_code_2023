
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


with open("puzzle_input.txt", "r") as inp:
    for line in inp:
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
startb = None

try:
    if map[top_nbr[1]][top_nbr[0]] == "|" or map[top_nbr[1]][top_nbr[0]] == "7" or map[top_nbr[1]][top_nbr[0]] == "F":
        starta = top_nbr
except:
    pass

try:
    if map[right_nbr[1]][right_nbr[0]] == "-" or map[right_nbr[1]][right_nbr[0]] == "7" or map[right_nbr[1]][right_nbr[0]] == "J":
        if starta is None:
            starta = right_nbr
        else:
            startb = right_nbr
except:
    pass

try:
    if map[bottom_nbr[1]][bottom_nbr[0]] == "|" or map[bottom_nbr[1]][bottom_nbr[0]] == "L" or map[bottom_nbr[1]][bottom_nbr[0]] == "J":
        if starta is None:
            starta = bottom_nbr
        else:
            startb = bottom_nbr
except:
    pass

try:
    if map[left_nbr[1]][left_nbr[0]] == "-" or map[left_nbr[1]][left_nbr[0]] == "F" or map[left_nbr[1]][left_nbr[0]] == "L":
        if starta is None:
            starta = left_nbr
        else:
            startb = left_nbr
except:
    pass

print(starta)
print(startb)
preva_x = startX
prevb_x = startX
preva_y = startY
prevb_y = startY

a_x = starta[0]
a_y = starta[1]
b_x = startb[0]
b_y = startb[1]

steps = 1
while a_x != b_x or a_y != b_y:
    #print(a_x)
    #print(a_y)
    # Move A
    temp_x = a_x
    temp_y = a_y
    (a_x,a_y) = get_next_location(a_x,a_y,preva_x,preva_y)
    preva_x = temp_x
    preva_y = temp_y

    # Move B
    temp_x = b_x
    temp_y = b_y 
    (b_x,b_y) = get_next_location(b_x,b_y,prevb_x,prevb_y)
    prevb_x = temp_x
    prevb_y = temp_y

    #print("A path next step: (" + str(a_x) + "," + str(a_y) + ")" )
    #print("B path next step: (" + str(b_x) + "," + str(b_y) + ")" )

    steps += 1


print(steps)