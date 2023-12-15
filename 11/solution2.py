map = []

expanded_rows = []
expanded_columns = []
i = 0
#with open("test_input.txt", "r") as inp:
with open("puzzle_input.txt", "r") as inp:
    for line in inp:
        map.append(line.strip())
        # expand rows
        if not "#" in line:
            expanded_rows.append(i)
        i += 1

#print(str(len(map)) + " " + str(len(map[0])))
#for line in map:
#    print(line)

# expand columns
len_line = len(map[0])
num_lines = len(map)
i=0
while i < len_line:
    #print("Checking column " + str(i))
    all_dots = True
    for j in range(num_lines):
        all_dots = all_dots and map[j][i] == "."
    if all_dots:
        #print("Inserting column at " + str(i))
        expanded_columns.append(i)
    i += 1

#for line in map:
#    print(line)
total_length = 0

#print(str(len(map)) + " " + str(len(map[0])))
# calculate distances
expansion_factor = 999999
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == "#":
            # we've hit a galaxy, calculate distance to the ones that follow.
            #print("Hit a galaxy: " + str(i) + "," + str(j))

            # first the rest of the line
            for l in range(j+1, len(map[0])):
                if map[i][l] == "#":
                    #print("Distance from " + str(i) + "," + str(j) + " to " + str(l) + " is " + str(l-j))
                    total_length += abs(l-j)
                    increment = 0
                    for x in expanded_columns:
                        if x > j and x < l:
                            increment += 1
                    total_length += (increment*expansion_factor)
            
            # now the other lines
            for k in range(i+1, len(map)):
                for l in range(len(map[0])):
                    #print(str(k) + " " + str(l))
                    #print("Distance from " + str(i) + "," + str(j) + " to " + str(k) + "," + str(l) + " is " + str(l-j))
                    if map[k][l] == "#":
                        total_length += abs(l-j)+abs(k-i)
                        increment = 0
                        for x in expanded_columns:
                            if (x > j and x < l) or (x > l and x < j):
                                increment += 1
                        for x in expanded_rows:
                            if x > i and x < k:
                                increment += 1
                        total_length += (increment*expansion_factor)

print(total_length)
