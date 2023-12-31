
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

platform = shiftNorth(platform)
load = calculateLoad(platform)
print(load)