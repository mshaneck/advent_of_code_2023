
map = {}
instructions = []
with open("puzzle_input.txt", "r") as inp:
#with open("/home/mshaneck/development/advent_of_code/advent_of_code_2023/18/test_input.txt", "r") as inp:
    for line in inp:
        line = line.strip()
        instructions.append(line.split())

map[0] = {}
map[0][0] = ("@", "ORIGIN")
x = 0
y = 0
for instruction in instructions:
    # U/L/D/R followed by number nad color
    #print("Current: (" + str(x) + ", " + str(y) + ")")
    #print(instruction)
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
    if dir == "L":
        for i in range(x-1, x-count-1, -1):
            map[y][i] = "<"
        if map[y][x] == "^":
            map[y][x] = "7"
        if map[y][x] == "v":
            map[y][x] = "J"
        x -= count 
    if dir == "R":
        for i in range(x+1, x+count+1):
            map[y][i] = ">"
        if map[y][x] == "^":
            map[y][x] = "F"
        if map[y][x] == "v":
            map[y][x] = "L"
        x += count 

max_y = 0
max_x = 0
min_x = 0
min_y = 0
for row in map:
    if row > max_y:
        max_y = row
    if row < min_y:
        min_y = row
    for column in map[row]:
        if column > max_x:
            max_x = column
        if column < min_x:
            min_x = column 

print("Min: (" + str(min_x) + ", " + str(min_y) + ")")
print("Max: (" + str(max_x) + ", " + str(max_y) + ")")

count = 0
line_count = 0
for y in range(min_y, max_y+1):
    line = ""
    outside = True
    onLine_fromtop = False
    onLine_frombottom = False
    for x in range(min_x, max_x+1):
        if x not in map[y]:
            map[y][x] = "."

        if map[y][x] == "^" or map[y][x] == "v":
            outside = not outside

        if map[y][x] == "F":
            onLine_frombottom = True
        if map[y][x] == "L":
            onLine_fromtop = True
        if map[y][x] == "J":
            if onLine_frombottom:
                outside = not outside
            onLine_frombottom = False
            onLine_fromtop = False
        if map[y][x] == "7":
            if onLine_fromtop:
                outside = not outside
            onLine_frombottom = False
            onLine_fromtop = False

        if map[y][x] == "." and not outside:
            map[y][x] = "#"
        
        if map[y][x] != ".":
            count += 1
        line += map[y][x] 

    print(line)
print(count)


