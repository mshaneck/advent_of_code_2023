import math
import numpy

def do_stones_hit(s1,s2):
    print("Checking for collision between: " + str(s1) + " and " + str(s2))
    timeToCollision = -1
    [[x1,y1,z1],[dx1,dy1,dz1]] = s1
    [[x2,y2,z2],[dx2,dy2,dz2]] = s2
    relativePos = [x2-x1,y2-y1]
    relativeVel = [dx2-dx1,dy2-dy1]
    relativeSpeed = math.sqrt(relativeVel[0]*relativeVel[0] + relativeVel[1]*relativeVel[1])
    distance = math.sqrt(relativePos[0]*relativePos[0] + relativePos[1]*relativePos[1])
    timeToCollision = numpy.dot(relativePos, relativeVel)
    #print(timeToCollision)
    if timeToCollision > 0:
        timeToCollision /= relativeSpeed * relativeSpeed 
        timeToCollision = int(timeToCollision)
        print("time to collision: " + str(int(timeToCollision)))
        minSeparation = distance - relativeSpeed * timeToCollision
        if minSeparation == 0:
            print("Collide at: " + str(timeToCollision))
        else:
            print("Min separation: " + str(minSeparation))

    return timeToCollision

def get_intersect(s1, s2):
    [[x1,y1,z1],[dx1,dy1,dz1]] = s1
    [[x2,y2,z2],[dx2,dy2,dz2]] = s2
    #print("Checking paths for " + str(s1) + " and " + str(s2))
    # should deal with dx1 or dx2 == 0, but that's not the case in the input so...
    m1 = dy1/dx1
    b1 = y1 - (m1*x1)
    m2 = dy2/dx2
    b2 = y2 - (m2*x2) 

    #print("y1 = " + str(m1)+"*x + " + str(b1))
    #print("y2 = " + str(m2)+"*x + " + str(b2))
    if m1-m2 == 0:
        return (-1,-1, -1)
    int_x = (b2-b1)/(m1-m2)
    int_y = m1*int_x + b1 
    time_to_intersect1 = (int_x-x1)/dx1
    time_to_intersect2 = (int_x-x2)/dx2
    return (int_x, int_y, min(time_to_intersect1, time_to_intersect2))

def get_x_extremes(t):
    global hailstones
    # return the min and max with respect to the x coordinate
    min_x = None
    max_x = None
    min_i = None 
    max_i = None 

    for i in range(len(hailstones)):
        s = hailstones[i]
        x = s[0][0] + s[1][0]*t
        if min_x is None or x < min_x:
            min_x = x 
            min_i = i
        if max_x is None or x > max_x:
            max_x = x
            max_i = i
    return (min_i, max_i)

def get_positions_at_t(t):
    global hailstones
    positions = []
    for s in hailstones:
        positions.append((s[0][0]+s[1][0]*t, s[0][1] + s[1][1]*t, s[0][2] + s[1][2]*t))
    return positions

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


print(total)