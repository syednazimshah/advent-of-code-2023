from math import prod

time = """47 84 74 67"""
distance = """207 1394 1209 1014"""

time = int(time.replace(" ", ""))
distance = int(distance.replace(" ", ""))


count = 0
for i in range(0, time):
    speed = i
    time_left = time-i

    if speed * time_left > distance:
        count+=1
print(count)

        