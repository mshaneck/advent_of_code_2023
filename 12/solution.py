
import re

springs = []

def check_pattern(springs, pattern):
    count = 0
    if "?" not in springs:
        if pattern.match(springs):
            count = 1
    else:
        count = 0
        count += check_pattern(springs.replace("?", ".", 1), pattern)
        count += check_pattern(springs.replace("?", "#", 1), pattern)
    return count

total = 0
with open("puzzle_input.txt", "r") as inp:
#with open("test_input.txt", "r") as inp:
    for line in inp:
        #print(line.strip())
        (springs, groups) = line.strip().split(" ")
        group_nums = groups.split(",")
        pattern_str = "^[.]*"
        first = True
        for num in group_nums:
            if first:
                first=False
                pattern_str += "[#]{" + str(num) + "}"
            else:
                pattern_str += "[.]+[#]{" + str(num) + "}"
        pattern_str += "[.]*$"
        #print(pattern_str)
        pattern = re.compile(pattern_str)
        total += check_pattern(springs, pattern)

print(total)
