
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

def getHorizontalMirror(m, horizontal, index):
    # find a horizontal line that is a mirror
    # start at 1 and end early since the mirror has to be between two rows or columns
    for i in range(1,len(m)):
        val = getHorizontalReflection(m, i)
        if not horizontal or val != index:
            if val == i:
                return i 
    return -1

def getVerticalMirror(m, horizontal, index):
    # find vertical line that is mirror
    for i in range(1, len(m[0])):
        val = getVerticalReflection(m, i)
        if horizontal or val != index:
            if val == i:
                return i
    return -1

def getMirror(m, horizontal, index):
    val = getHorizontalMirror(m, horizontal, index)
    if val != -1:
        return (True, val) 
    else:
        val = getVerticalMirror(m, horizontal, index)
        if val != -1:
            return (False, val) 
    return (False, -1)

maps = []
m = []
#with open("/home/mshaneck/development/advent_of_code/advent_of_code_2023/13/test_input.txt", "r") as inp:
with open("puzzle_input.txt", "r") as inp:
    for line in inp:
        line = line.strip()
        if line == "":
            maps.append(m)
            m = []
        else:
            m.append(list(line))
maps.append(m)

total = 0
num = 0
for mp in maps:
    #print("*"*50)
    #print("*"*50)
    (horizontal, index) = getMirror(mp, False, -1)
    #print(str(horizontal) + ", " + str(index))
    breakOut = False
    added_new = False
    for i in range(0,len(mp)):
        for j in range(0,len(mp[0])):
            # Test if smudge is here
            #print(str(i) + "," + str(j))
            orig_value = mp[i][j]
            if mp[i][j] == "#":
                mp[i][j] = "."
            else:
                mp[i][j] = "#"
            """ for m in mp:
                print(''.join(m)) """

            (new_horizontal, new_index) = getMirror(mp, horizontal, index)
            #print(str(new_horizontal) + ", " + str(new_index))
            if new_index >= 0 and (new_horizontal != horizontal or new_index != index):
                added_new = True
                #print("*"*50)
                for m in mp:
                    print(''.join(m))
                #print("New Mirror found. Horizontal: " + str(new_horizontal) + " at index " + str(new_index))
                if new_horizontal:
                    total += 100*new_index
                else:
                    total += new_index
                breakOut = True
                break
            #restore smudge
            mp[i][j] = orig_value
        if breakOut:
            break
    if not added_new:
        print("Did not add a new one.")
    num+=1
print(total)
