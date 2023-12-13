
def get_prev_seq_num(seq_and_diffs):
    # iterate through the last items in the list in reverse, starting with the 0
    increment = 0
    for i in range(2, len(seq_and_diffs)):
        increment = seq_and_diffs[-1*i][0] - increment
        print(increment)
    return  seq_and_diffs[0][0] - increment

seqs = []
with open("puzzle_input.txt", "r") as inp:
    for line in inp:
        seqs.append([int(x) for x in line.split()])

seq_and_diffs = {}
count = 0
for seq in seqs:
    seq_and_diffs[count] = []
    seq_and_diffs[count].append(seq)
    all_zeros = False
    to_check = seq
    while not all_zeros:
        diffs = []
        all_zeros = True
        for i in range(len(to_check)):
            if i < len(to_check)-1:
                diff = to_check[i+1] - to_check[i]
                diffs.append(diff)
                all_zeros = all_zeros and (diff==0)
        seq_and_diffs[count].append(diffs)
        to_check = diffs

    count += 1

print(seq_and_diffs)
total = 0
for i in seq_and_diffs:
    total += get_prev_seq_num(seq_and_diffs[i])
print(total)