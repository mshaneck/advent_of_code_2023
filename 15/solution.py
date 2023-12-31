
def hash(inp):
    current_value = 0
    for c in inp:
        current_value += ord(c)
        current_value *= 17
        current_value = current_value % 256
    return current_value

with open("puzzle_input.txt", "r") as inp:
#with open("test_input.txt", "r") as inp:
    hash_value = 0
    for line in inp:
        for inst in line.strip().split(","):
            hash_value += hash(inst)
        
    print(hash_value)