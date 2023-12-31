
def getHorizontalReflection(m, index):
    # is the given index a reflection mirror
    # the index is not going to be 0 or length(m)-1
    # and for index, the mirror is between index-1 and index
    i=index-1
    j=index
    #print(len(m))
    while i >= 0 and j < len(m):
        #print("Checking line " + str(i) + " against " + str(j))
        if m[i] != m[j]:
            return -1
        i-=1
        j+=1
    return index

def getVerticalReflection(m, index):
    i = index-1
    j = index 
    while i >= 0 and j < len(m[0]):
        # need to do the whole line
        for k in range(0,len(m)):
            if m[k][i] != m[k][j]:
                return -1
        i-=1
        j+=1
    return index

def getHorizontalMirror(m):
    # find a horizontal line that is a mirror
    # start at 1 and end early since the mirror has to be between two rows or columns
    for i in range(1,len(m)):
        val = getHorizontalReflection(m, i)
        if val == i:
            return i 
    return -1

def getVerticalMirror(m):
    # find vertical line that is mirror
    for i in range(1, len(m[0])):
        val = getVerticalReflection(m, i)
        if val == i:
            return i
    return -1

maps = []
m = []
with open("/home/mshaneck/development/advent_of_code/advent_of_code_2023/13/test_input.txt", "r") as inp:
#with open("puzzle_input.txt", "r") as inp:
    for line in inp:
        line = line.strip()
        if line == "":
            maps.append(m)
            m = []
        else:
            m.append(line)
maps.append(m)

total = 0
num = 0
for mp in maps:
    val = getHorizontalMirror(mp)
    if val != -1:
        print("Horizontal mirror for map " + str(num) + " found at index: " + str(val))
        for l in mp:
            print(l)
        print("*"*40)
        total += 100*val 
    else:
        val = getVerticalMirror(mp)
        if val != -1:
            print("Vertical mirror for map " + str(num) + " found at index: " + str(val))
            for l in mp:
                print(l)
            print("*"*40)
            total += val 
        else:
            print("*"*40 + "No mirror found... for map " + str(num))
            for l in mp:
                print(l)
            print("*"*40)
    num+=1
print(total)
