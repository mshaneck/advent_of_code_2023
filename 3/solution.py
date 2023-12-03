
def isSymbol(c):
    return c != "." and c != "\n" and not c.isdigit() 

def isNumberPart(prevL, currentL, nextL, start, end):
    # search prev/next from start-1 to end and current at both those places
    print("Testing " + currentL[start:end])
    print(start)
    print(end)
    retVal = False
    for i in range(start-1, end+1):
        if prevL is not None and not i >= len(prevL) and not i < 0:
            retVal = retVal or isSymbol(prevL[i])
        if nextL is not None and not i >= len(nextL) and not i < 0:
            retVal = retVal or isSymbol(nextL[i])
    retVal = retVal or isSymbol(currentL[start-1])
    if not end >= len(currentL):
        retVal = retVal or isSymbol(currentL[end])
    return retVal

def getPartNumbers(prevL, currentL, nextL):
    startNum = -1
    endNum = -1
    findingNum = False 
    partNumbers = []

    if currentL is not None:
        for i in range(len(currentL)):
            if currentL[i].isdigit() and not findingNum:
                findingNum = True
                startNum=i 
            if not currentL[i].isdigit() and findingNum:
                findingNum = False
                endNum=i
                if isNumberPart(prevL, currentL, nextL, startNum, endNum):
                    partNumbers.append(int(currentL[startNum:endNum]))

    return partNumbers

def getPartNumSum(previous_line, current_line, next_line):
    total=0
    print("#"*100)
    print(previous_line)
    print(current_line)
    print(next_line)
    partNumbers = getPartNumbers(previous_line, current_line, next_line)
    print(partNumbers)
    for part in partNumbers:
        total += part
    return total

with open("puzzle_input.txt", "r") as inp:
    previous_line = None
    current_line = None
    next_line = None
    total = 0
    
    for line in inp:
        previous_line = current_line
        current_line = next_line
        next_line = line 
        total += getPartNumSum(previous_line, current_line, next_line)

    previous_line = current_line
    current_line = next_line
    next_line = None
    total += getPartNumSum(previous_line, current_line, next_line)

    print(total)
