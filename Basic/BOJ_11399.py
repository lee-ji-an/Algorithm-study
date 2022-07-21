min_idx = 0
time = 0
total_time = 0

p_num = int(input())
p_time = input().split()

for i in range(len(p_time)):
    p_time[i] = int(p_time[i])

for j in range(p_num):
    for i in range(len(p_time)):
        if p_time[min_idx] > p_time[i]:
            min_idx = i
    time = time + p_time[min_idx]
    p_time[min_idx] = 1001
    total_time = total_time + time
print(total_time)