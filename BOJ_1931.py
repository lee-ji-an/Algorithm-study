import sys

n = int(sys.stdin.readline())
time_table = [[0]*2 for _ in range(n)]
for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    time_table[i][0] = s
    time_table[i][1] = e

time_table.sort(key = lambda x: (x[1], x[0]))
cnt = 0
end = 0

for i in range(len(time_table)):
    if end <= time_table[i][0]:
        cnt = cnt + 1
        end = time_table[i][1]
print(cnt)