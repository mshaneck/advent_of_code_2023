

with open("puzzle_input.txt", "r") as inp:
    count = 1
    total = 0
    for line in inp:
        #Card   1:  4 33 89 61 95 36  5 30 26 55 | 15 33 28 36 93 57 26 13 95  4 18 79  6 87 60 66 69 67 19 42 22 61 78  5 58
        (card, numbers) = line.split(":")
        (winning_numbers, our_numbers) = numbers.split("|")
        nums = our_numbers.split(" ")
        matches = 0
        for num in nums:
            try:
                n = int(num)
                str_n = " " + str(n) + " "
                #print ("Checking if '" + str_n + "' is in '" + winning_numbers + "'")
                if str_n in winning_numbers:
                    matches += 1
            except:
                # This is a space, so just skip over it
                pass

        #print("Card " + str(count) + " has " + str(matches) + " matches")
        if matches > 0:
            total += 2**(matches-1)
        count+=1
    print(total)