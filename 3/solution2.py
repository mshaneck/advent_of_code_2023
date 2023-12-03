
def getGearNumbers(numberLine, j):
    retNumbers = []
    for number in numberLine:
        if j >= number[1]-1 and j <= number[2]+1:
            retNumbers.append(number[0])
    return retNumbers

def getGearRatio(i, j, numbers):
    nums = []

    # j is the column of the star
    # need to look in numbers[i-1], numbers[i], and numbers[i+1] if they exist
    if i > 0:
        # look in numbers[i-1]
        nums.extend(getGearNumbers(numbers[i-1], j))
    nums.extend(getGearNumbers(numbers[i], j))
    if i < len(numbers)-1:
        nums.extend(getGearNumbers(numbers[i+1], j))

    total = 0
    if len(nums) > 1:
        print(nums)
        total = 1
        for num in nums:
            total *= num
    return total


def getNumbers(line):
    startNum = -1
    endNum = -1
    findingNum = False 
    partNumbers = []

    for i in range(len(line)):
        if line[i].isdigit() and not findingNum:
            findingNum = True
            startNum=i 
        if not line[i].isdigit() and findingNum:
            findingNum = False
            endNum=i-1
            partNumbers.append((int(line[startNum:endNum+1]), startNum, endNum))

    return partNumbers

with open("puzzle_input.txt", "r") as inp:

    total = 0
    numbers = []
    lines = []

    for line in inp:
        numbers.append(getNumbers(line))
        lines.append(line)

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "*":
                # potential gear - find if there are numbers adjacent
                total += getGearRatio(i, j, numbers)


    #print(numbers)
    print(total)
