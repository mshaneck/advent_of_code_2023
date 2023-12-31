
map = {}
instructions = []
with open("puzzle_input.txt", "r") as inp:
#with open("/home/mshaneck/development/advent_of_code/advent_of_code_2023/18/test_input.txt", "r") as inp:
    for line in inp:
        line = line.strip()
        parts = line.split()
        color = parts[2].replace("(","").replace(")","").replace("#","")
        distance = int(color[:5], 16)
        direction = color[5]
        #  0 means R, 1 means D, 2 means L, and 3 means U.
        if direction == "0":
            direction = "R"
        elif direction == "1":
            direction = "D"
        elif direction == "2":
            direction = "L"
        elif direction == "3":
            direction = "U"
        instructions.append((direction, distance))

map[0] = {}
map[0][0] = ("@", "ORIGIN")
x = 0
y = 0
shoelace = 0
shoe_x = 0
shoe_y = 0
for instruction in instructions:
    # U/L/D/R followed by number nad color
    #print("Current: (" + str(x) + ", " + str(y) + ")")
    #print(instruction)

    # shoelace
    # A = 1 / 2 (x0y1 − x1y0 + . . . + xn−2yn−1 − xn−1yn−2 + xn−1y0 − x0yn−1) .
    prev_x = x
    prev_y = y
    dir = instruction[0]
    count = int(instruction[1])
    if dir == "U":
        for j in range(y-1, y-count-1, -1):
            if j not in map:
                map[j] = {}
            map[j][x] = "^"
        
        if map[y][x] == ">":
            map[y][x] = "J"
        if map[y][x] == "<":
            map[y][x] = "L"
        y -= count 
        shoe_x = x 
        shoe_y = y
    if dir == "D":
        for j in range(y+1, y+count+1):
            if j not in map:
                map[j] = {}
            map[j][x] = "v"
        if map[y][x] == ">":
            map[y][x] = "7"
        if map[y][x] == "<":
            map[y][x] = "F"
        y += count 
        shoe_x = x 
        shoe_y = y
    if dir == "L":
        for i in range(x-1, x-count-1, -1):
            map[y][i] = "<"
        if map[y][x] == "^":
            map[y][x] = "7"
        if map[y][x] == "v":
            map[y][x] = "J"
        x -= count 
        shoe_x = x
        shoe_y = y
    if dir == "R":
        for i in range(x+1, x+count+1):
            map[y][i] = ">"
        if map[y][x] == "^":
            map[y][x] = "F"
        if map[y][x] == "v":
            map[y][x] = "L"
        x += count 
        shoe_x = x
        shoe_y = y
    
    # so add prev_x*y - x*prev_y for the shoelace
    shoelace += (prev_x)*(shoe_y) - (shoe_x)*(prev_y) + count

#print("Test should be \n952408144115")
print(1+shoelace//2)
