import re
from itertools import pairwise
import threading

seeds = []
map_pattern = re.compile("[0-9]+ [0-9]+ [0-9]+")
maps = {}
maps["seed-to-soil"] = []
maps["soil-to-fertilizer"] = []
maps["fertilizer-to-water"] = []
maps["water-to-light"] = []
maps["light-to-temperature"] = []
maps["temperature-to-humidity"] = []
maps["humidity-to-location"] = []

def get_destination_value(m, input_value, map_state):
    # look through maps[map_state] for a line where the input value is between [1] and [1]+[2], then the output is input_value-[1]+[0]
    # format is [destination, source, range]
    for valuemap in m[map_state]:
        destination = valuemap[0]
        source = valuemap[1]
        map_range = valuemap[2]
        if input_value >= source and input_value < source+map_range:
            return input_value-source+destination

    # if they don't fall into any of these ranges, then the output is the same as input
    return input_value

def get_location_for_seed(seed, m):
    soil  = get_destination_value(m, seed, "seed-to-soil")
    fert  = get_destination_value(m, soil, "soil-to-fertilizer")
    water = get_destination_value(m, fert, "fertilizer-to-water")
    light = get_destination_value(m, water, "water-to-light")
    temp  = get_destination_value(m, light, "light-to-temperature")
    humid = get_destination_value(m, temp, "temperature-to-humidity")
    loc   = get_destination_value(m, humid, "humidity-to-location")
    return loc

#with open("test_input.txt", "r") as inp:
with open("puzzle_input.txt", "r") as inp:
    state = "seeds"
    for line in inp:
        line = line.strip()
        if line == "":
            continue
        elif line[0:5] == "seeds":
            # read in the seeds line
            #print(line.split(":")[1].split(" "))
            seeds = [int(x) for x in line.split(":")[1].strip().split(" ")]
        elif line[0:5] == "seed-":
            state = "seed-to-soil"
        elif line[0:5] == "soil-":
            state = "soil-to-fertilizer"
        elif line[0:5] == "ferti":
            state = "fertilizer-to-water"
        elif line[0:5] == "water":
            state = "water-to-light"
        elif line[0:5] == "light":
            state = "light-to-temperature"
        elif line[0:5] == "tempe":
            state = "temperature-to-humidity"
        elif line[0:5] == "humid":
            state = "humidity-to-location"
        elif map_pattern.match(line):
            values = [int(x) for x in line.split(" ")]
            maps[state].append(values)

seed_ranges = []
for i in range(0, len(seeds), 2):
    seed_ranges.append([seeds[i], seeds[i+1]])

#print(seed_ranges)
lowest_seed = seed_ranges[0][0]
lowest_location = get_location_for_seed(lowest_seed,maps)

seeds_counted = 0

def search_range(start,end, m):
    #print("Starting search process from " + str(start) + " to " + str(end))
    #print(str(end-start) + " seeds ")
    global lowest_seed 
    global lowest_location 
    global seeds_counted
    i = start
    while i < end:
        current_loc = get_location_for_seed(i,m)
        if current_loc < lowest_location:
            if current_loc == 0:
                print("WE GOT A ZERO")
            lowest_location = current_loc
            lowest_seed = i
            #print("lowest seed: " + str(lowest_seed))
            #rint("lowest location: " + str(lowest_location))
        increment = 1000000

        jump_loc = get_location_for_seed(i+increment,m)
        # let's jump as much as we can, starting with 1 million, dividing that increment by 10 each time the jump won't work
        # minimum jump of 1
        while (jump_loc != current_loc+increment or i+increment >= end)  and increment>1:
            increment = increment // 10
            jump_loc = get_location_for_seed(i+increment,m)
        
        i+= increment
        #print("Jump: " + str(increment))
    seeds_counted += (i-start)
    #print("counted: " + str(i-start))

#print("LOWEST LOCATION: " + str(lowest_location))
to_count = 0
for seed_range in seed_ranges:
    to_count += (seed_range[1])
    i = seed_range[0] # first seed
    n = seed_range[0]+seed_range[1] # last seed 
    search_range(i, n, maps)

print("lowest seed: " + str(lowest_seed))
print("lowest location: " + str(lowest_location))
#print("Seeds counted: " + str(seeds_counted))
#print("To count: " + str(to_count))
