import math

moves = "LLRLRLLRRLRLRLLRRLRRRLRRRLRRLRRLRLRLRRRLLRLRRLRLRRRLRLLRRLRLRLLRRRLLRLRRRLRLRRLRRLRLLRRLRRLRLRLRLLRLLRRLRRLRRLRRLRRLRLLRLRLRRRLRRRLRRLRLRLRRLRRRLRLRRRLRLRLRLRRRLRRLRRLRRRLLLLRRLRRLRLRRRLRLRRRLRRLLLLRLRLRRRLRRRLRLRRLLRLRLRRRLRLRLRRRLRLLRRRLRRLRLRLRRRLRLLRRLLRRRLRRRLRRRLRRLRLRLRRRLRRRLRRRLLRRRR"

map_nodes = {}
starting_nodes = []

with open("puzzle_input.txt", "r") as inp:
    for line in inp:
        (location, nbrs) = line.split("=")
        (l,r) = nbrs.replace("(", "").replace(")","").split(",")
        location = location.strip()
        map_nodes[location] = (l.strip(), r.strip())
        if location[2] == "A":
            starting_nodes.append(location)

print("Starting nodes: " + str(starting_nodes))
move_counts = []

for start_node in starting_nodes:
    move_index = 0
    move_count = 0
    current_location = start_node
    while current_location[2] != "Z":
        move = moves[move_index]
        move_to = 0
        if move == "R":
            move_to = 1
        current_location = map_nodes[current_location][move_to]
        move_count += 1
        #print(current_location + " in " + str(move_count) + " moves")
        # cycle back around if needed
        move_index = (move_index+1)%len(moves)
    move_counts.append(move_count)

lcm = 1
for i in move_counts:
    lcm = lcm*i//math.gcd(lcm,i)

print(lcm)
