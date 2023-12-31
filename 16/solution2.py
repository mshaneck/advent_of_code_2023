import sys
sys.setrecursionlimit(5000)

tiles = [] # this contains the mirrors and splitters
light = [] # this contains the light directions

def shoot_beam(i, j, direction):
    global tiles
    global light
    if i >= 0 and i < len(tiles) and j >= 0 and j < len(tiles[i]):
        if light[i][j] is None or direction not in light[i][j]:
            if light[i][j] is None:
                light[i][j] = [direction]
            else:
                light[i][j].append(direction)
            if tiles[i][j] == "\\":
                if direction == ">":
                    shoot_beam(i+1,j,"v")
                elif direction == "<":
                    shoot_beam(i-1,j,"^")
                elif direction == "v":
                    shoot_beam(i,j+1,">")
                elif direction == "^":
                    shoot_beam(i,j-1,"<")
            elif tiles[i][j] == "/":
                if direction == ">":
                    shoot_beam(i-1,j,"^")
                elif direction == "<":
                    shoot_beam(i+1,j,"v")
                elif direction == "v":
                    shoot_beam(i,j-1,"<")
                elif direction == "^":
                    shoot_beam(i,j+1,">")
            elif tiles[i][j] == "-":
                if direction == ">":
                    shoot_beam(i,j+1,">")
                elif direction == "<":
                    shoot_beam(i,j-1,"<")
                elif direction == "v" or direction == "^":
                    shoot_beam(i,j-1,"<")
                    shoot_beam(i,j+1,">")
            elif tiles[i][j] == "|":
                if direction == "^":
                    shoot_beam(i-1,j,"^")
                elif direction == "v":
                    shoot_beam(i+1,j,"v")
                elif direction == "<" or direction == ">":
                    shoot_beam(i-1,j,"^")
                    shoot_beam(i+1,j,"v")
            else:
                if direction == ">":
                    shoot_beam(i,j+1,">")
                elif direction == "<":
                    shoot_beam(i,j-1,"<")
                elif direction == "v":
                    shoot_beam(i+1,j,"v")
                elif direction == "^":
                    shoot_beam(i-1,j,"^")

def total_lit_tiles():
    global light
    lit = 0
    for i in range(len(light)):
        for j in range(len(light[i])):
            if light[i][j] is not None:
                lit += 1
    return lit

with open("puzzle_input.txt", "r") as inp:
#with open("test_input.txt", "r") as inp:
    for line in inp:
        tiles.append(list(line.strip()))
        light.append([None] * len(line.strip()))

def blank_light():
    global light
    for i in range(len(light)):
        light[i] = [None] * len(light[i])

max_lit = 0
# shoot the beam left and right all along the sides
for i in range(len(tiles)):
    blank_light()
    shoot_beam(i,0,">")
    lit = total_lit_tiles()
    if lit > max_lit:
        max_lit = lit 
    blank_light()
    shoot_beam(i,len(tiles[i])-1,"<")
    lit = total_lit_tiles()
    if lit > max_lit:
        max_lit = lit 

# shoot the beam up and down all along the top and bottom
        
for j in range(len(tiles[0])):
    blank_light()
    shoot_beam(0,j,"v")
    lit = total_lit_tiles()
    if lit > max_lit:
        max_lit = lit 
    blank_light()
    shoot_beam(len(tiles)-1,j,"^")
    lit = total_lit_tiles()
    if lit > max_lit:
        max_lit = lit 
    
print(max_lit)
