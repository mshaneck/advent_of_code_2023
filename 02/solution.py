import re

red_limit=12
green_limit=13
blue_limit=14

total=0

with open("puzzle_input.txt", "r") as games:
    for game in games:
        parts = game.split(":")
        game_number = int(parts[0][5:])
        draws = parts[1].strip().split(";")

        valid = True
        for draw in draws:
            cubes = draw.strip().split(",")
            for cube in cubes:
                (number, color) = cube.strip().split(" ")
                if (color == "red"   and int(number) > red_limit) or \
                   (color == "green" and int(number) > green_limit) or \
                   (color == "blue"  and int(number) > blue_limit):
                    valid=False
        if valid:
            total += game_number

print(total)

