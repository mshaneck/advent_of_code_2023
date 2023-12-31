
def get_intersect(s1, s2):
    [[x1,y1,z1],[dx1,dy1,dz1]] = s1
    [[x2,y2,z2],[dx2,dy2,dz2]] = s2
    # should deal with dx1 or dx2 == 0, but that's not the case in the input so...
    m1 = dy1/dx1
    b1 = y1 - (m1*x1)
    m2 = dy2/dx2
    b2 = y2 - (m2*x2) 

    if m1-m2 == 0:
        return (-1,-1, -1)
    int_x = (b2-b1)/(m1-m2)
    int_y = m1*int_x + b1 
    time_to_intersect1 = (int_x-x1)/dx1
    time_to_intersect2 = (int_x-x2)/dx2
    return (int_x, int_y, min(time_to_intersect1, time_to_intersect2))

hailstones = []

with open("puzzle_input.txt", "r") as inp:
#with open("/home/mshaneck/development/advent_of_code/advent_of_code_2023/24/test_input.txt", "r") as inp:
    for line in inp:
        line = line.strip()
        position = [int(x) for x in line.split("@")[0].split(",")]
        velocity = [int(x) for x in line.split("@")[1].split(",")]
        hailstones.append([position, velocity, -1])

bound_min = 200000000000000
bound_max = 400000000000000

total = 0
for i in range(len(hailstones)):
    for j in range(i+1, len(hailstones)):
        s1 = hailstones[i]
        s2 = hailstones[j]
        (x,y,t) = get_intersect(s1[0:2], s2[0:2])
        # is the intersection within the proper bounds
        if t >= 0 and bound_min <= x and x <= bound_max and bound_min <= y and y <= bound_max:
            hailstones[i][2] = t
            hailstones[j][2] = t
            total += 1

print(total)