
def cycle(platform):
    platform = shiftNorth(platform)
    platform = shiftWest(platform)
    platform = shiftSouth(platform)
    platform = shiftEast(platform)
    return platform

def shiftNorth(platform):
    # Can start at 1 since the first row can't move up anyway
    for i in range(1, len(platform)):
        for j in range(0, len(platform[0])):
            # if this is a O, shift it up until it hits another O or a # or the edge.
            if platform[i][j] == "O":
                k = i-1
                while k >= 0:
                    if platform[k][j] == "O" or platform[k][j] == "#":
                        break
                    else:
                        # It can move up one.
                        platform[k][j] = "O"
                        platform[k+1][j] = "."
                    k -= 1
    return platform

def shiftSouth(platform):
    for i in range(len(platform)-2, -1, -1):
        for j in range(0, len(platform[0])):
            # if this is a O, shift it up until it hits another O or a # or the edge.
            if platform[i][j] == "O":
                k = i+1
                while k < len(platform):
                    if platform[k][j] == "O" or platform[k][j] == "#":
                        break
                    else:
                        # It can move up one.
                        platform[k][j] = "O"
                        platform[k-1][j] = "."
                    k += 1
    return platform

def shiftEast(platform):
    for j in range(len(platform[0])-2, -1, -1):
        for i in range(0, len(platform)):
            # if this is a O, shift it right until it hits another O or a # or the edge.
            if platform[i][j] == "O":
                k = j+1
                while k < len(platform[0]):
                    if platform[i][k] == "O" or platform[i][k] == "#":
                        break
                    else:
                        # It can move up one.
                        platform[i][k] = "O"
                        platform[i][k-1] = "."
                    k += 1
    return platform

def shiftWest(platform):
    for j in range(0, len(platform[0])):
        for i in range(0, len(platform)):
            # if this is a O, shift it right until it hits another O or a # or the edge.
            if platform[i][j] == "O":
                k = j-1
                while k >= 0:
                    if platform[i][k] == "O" or platform[i][k] == "#":
                        break
                    else:
                        # It can move up one.
                        platform[i][k] = "O"
                        platform[i][k+1] = "."
                    k -= 1
    return platform

def calculateLoad(platform):
    total = 0
    for i in range(0, len(platform)):
        for j in range(0, len(platform[0])):
            if platform[i][j] == "O":
                total += len(platform)-i
    return total 

platform = []

with open("puzzle_input.txt", "r") as inp:
#with open("test_input.txt", "r") as inp:
    for line in inp:
        line = line.strip()
        platform.append(list(line))

cycles = 1000000000
cycles = 100
for i in range(cycles):
    if i > 0 and i % 1000000 == 0:
        print("1 more million")
    platform = cycle(platform)
    load = calculateLoad(platform)
    """ if load == 96141:
        print(str(load) + "*"*20 + " " + str(i))
    else:
        print(load)    """ 
# cycle length is 11, from manual inspection
# cycles start at index 95 (96th cycle)

# cycle 1000000000 should be at offset 2 from the cycle: 96105
cycle_contents = [96141, 96124, 96105, 96094, 96097, 96095 , 96093, 96096, 96112, 96132, 96141]
print(cycle_contents[(1000000000-96)%11])