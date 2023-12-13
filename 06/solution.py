
races = {47: 282, 70: 1079, 75:1147, 66:1062}

def get_distance(hold_time, run_time):
    # hold time is speed
    # so distance is just run_time*hold_time
    return hold_time * run_time

def defeat_count(time, dist_record):
    win_count = 0
    for i in range(time+1):
        distance = get_distance(i, time-i)
        if distance > dist_record:
            win_count += 1
    return win_count

win_prod=1
for x in races:
    win_prod *= defeat_count(x, races[x])

print(win_prod)