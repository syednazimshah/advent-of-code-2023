from math import prod

time = """47 84 74 67"""
distance = """207 1394 1209 1014"""

time_list = time.split(" ")
dis_list = distance.split(" ")
list_result = []
for each in time_list:
    total_time = int(each)
    count = 0
    for i in range(0, total_time):
        speed = i
        time_left = total_time-i

        if speed * time_left > int(dis_list[time_list.index(each)]):
            count+=1
    print(count)
    list_result.append(count)

print(prod(list_result))
        