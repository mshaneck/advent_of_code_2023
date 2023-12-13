import re

total=0

with open("puzzle_input.txt", "r") as games:
    for game in games:
        parts = game.split(":")
        game_number = int(parts[0][5:])
        draws = parts[1].strip().split(";")
        
        red_min=-1
        green_min=-1
        blue_min=-1

        for draw in draws:
            cubes = draw.strip().split(",")
            for cube in cubes:
                (number, color) = cube.strip().split(" ")
                if color=="red" and int(number) > red_min:
                    red_min = int(number)
                if color=="green" and int(number) > green_min:
                    green_min = int(number)
                if color=="blue" and int(number) > blue_min:
                    blue_min = int(number)
        total+= (red_min*blue_min*green_min)

print(total)

