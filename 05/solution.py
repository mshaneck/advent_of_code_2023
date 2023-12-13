import re

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

def get_destination_value(input_value, map_state):
    # look through maps[map_state] for a line where the input value is between [1] and [1]+[2], then the output is input_value-[1]+[0]
    # format is [destination, source, range]
    for valuemap in maps[map_state]:
        destination = valuemap[0]
        source = valuemap[1]
        map_range = valuemap[2]
        if input_value >= source and input_value <= source+map_range:
            print("Input value: " + str(input_value) + " is in range " + str(source) + ", " + str(source+map_range))
            print("Maps to " + str(input_value-source+destination))
            return input_value-source+destination

    # if they don't fall into any of these ranges, then the output is the same as input
    return input_value

def get_location_for_seed(seed):
    soil  = get_destination_value(seed, "seed-to-soil")
    fert  = get_destination_value(soil, "soil-to-fertilizer")
    water = get_destination_value(fert, "fertilizer-to-water")
    light = get_destination_value(water, "water-to-light")
    temp  = get_destination_value(light, "light-to-temperature")
    humid = get_destination_value(temp, "temperature-to-humidity")
    loc   = get_destination_value(humid, "humidity-to-location")
    return loc

#with open("test_input.txt", "r") as inp:
with open("puzzle_input.txt", "r") as inp:
    state = "seeds"
    for line in inp:
        line = line.strip()
        print(line[0:5])
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
            print(state)
            print(line)
            values = [int(x) for x in line.split(" ")]
            maps[state].append(values)

print(maps)
locations = []

for seed in seeds:
    print(seed)
    locations.append(get_location_for_seed(seed))

locations.sort()
print(locations)
