
moves = "LLRLRLLRRLRLRLLRRLRRRLRRRLRRLRRLRLRLRRRLLRLRRLRLRRRLRLLRRLRLRLLRRRLLRLRRRLRLRRLRRLRLLRRLRRLRLRLRLLRLLRRLRRLRRLRRLRRLRLLRLRLRRRLRRRLRRLRLRLRRLRRRLRLRRRLRLRLRLRRRLRRLRRLRRRLLLLRRLRRLRLRRRLRLRRRLRRLLLLRLRLRRRLRRRLRLRRLLRLRLRRRLRLRLRRRLRLLRRRLRRLRLRLRRRLRLLRRLLRRRLRRRLRRRLRRLRLRLRRRLRRRLRRRLLRRRR"

map_nodes = {}

with open("puzzle_input.txt", "r") as inp:
    for line in inp:
        (location, nbrs) = line.split("=")
        (l,r) = nbrs.replace("(", "").replace(")","").split(",")
        map_nodes[location.strip()] = (l.strip(), r.strip())

move_index = 0
move_count = 0
current_location = "AAA"

while current_location != "ZZZ":
    move = moves[move_index]
    move_to = 0
    if move == "R":
        move_to = 1
    current_location = map_nodes[current_location][move_to]
    move_count += 1
    #print(current_location + " in " + str(move_count) + " moves")
    # cycle back around if needed
    move_index = (move_index+1)%len(moves)

print(move_count)
