
def hash(inp):
    current_value = 0
    for c in inp:
        current_value += ord(c)
        current_value *= 17
        current_value = current_value % 256
    return current_value

def equals_op(box_num, label, focal):
    global boxes
    if not box_num in boxes:
        boxes[box_num] = []
    # if label exists in the list, replace the lens, if not, append
    for i in range(len(boxes[box_num])):
        if boxes[box_num][i][0] == label:
            boxes[box_num][i][1] = focal
            return
    boxes[box_num].append([label, focal])

def minus_op(box_num, label):
    global boxes
    if not box_num in boxes:
        boxes[box_num] = []
    for i in range(len(boxes[box_num])):
        if boxes[box_num][i][0] == label:
            boxes[box_num].pop(i)
            return

def calculate_focal_power():
    global boxes
    total = 0
    for i in boxes:
        for j in range(len(boxes[i])):
            total += (i+1)*(j+1)*boxes[i][j][1]
    return total

boxes = {}
with open("puzzle_input.txt", "r") as inp:
#with open("test_input.txt", "r") as inp:
    hash_value = 0
    for line in inp:
        for inst in line.strip().split(","):
            label = None
            focal = None
            if "=" in inst:
                (label, focal) = inst.split("=")
                box_num = hash(label)
                equals_op(box_num, label, int(focal))
            else:
                label = inst[:-1]
                box_num = hash(label)
                minus_op(box_num, label)

print(calculate_focal_power())        
