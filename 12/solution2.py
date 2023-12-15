import functools

def fits(springs, length, index):
    fits = index+length <= len(springs) and \
            not "." in springs[index:index+length] and \
            (index+length == len(springs) or springs[index+length] != "#") and \
            (index == 0 or springs[index-1] != "#")

    return fits

@functools.cache
def check_pattern(springs, groups, start_index):#, pattern_so_far):
    count = 0
    if len(groups) == 0:
        # if it made it to the end, it fits, since we fit all the groups in
        # one thing remains - are there any "#" left?
        if "#" in springs[start_index:]:
             return 0
        return 1
    
    group = int(groups[0])
    for index in range(start_index,len(springs)):
        if fits(springs, group, index):
            count += check_pattern(springs, groups[1:], index+group+1)#, pattern_so_far + "#"*group + ".")

        # if the current value is # then the remaining search should be abandoned
        # as we can't leave unmatched # characters
        if index < len(springs) and springs[index] == "#":
            return count
    return count

total = 0
line_count = 1
springs = []
expansion = 4
with open("puzzle_input.txt", "r") as inp:
    for line in inp:
        line_count += 1
        (springs, groups) = line.strip().split(" ")
        springs = (springs + "?")*expansion + springs
        groups = (groups + ",")*expansion + groups
        group_nums = groups.split(",")
        update = check_pattern(springs, tuple(group_nums), 0)
        total += update

print(total)
