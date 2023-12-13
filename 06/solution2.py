time = 47707566
dist_record = 282107911471062

count = 0
win_count = 0
for i in range(time+1):
    distance = i*(time-i)
    if distance > dist_record:
        win_count += 1
    count += 1
    
print(win_count)
