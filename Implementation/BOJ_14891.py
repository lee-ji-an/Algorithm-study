import sys
from collections import deque
input = sys.stdin.readline

wheel = [0]
for i in range(4):
    wheel.append(deque(list(input().rstrip())))

K = int(input())
command = []
for k in range(K):
    command.append(tuple(map(int, input().split())))

for number, direction in command:
    move_wheel = [(number, direction)]

    # 오른쪽에 위치한 톱니바퀴 탐색
    for i in range(number, 4):
        if wheel[i][2] == wheel[i + 1][6]:
            break
        move_wheel.append((i + 1, direction * (-1) ** (i - number + 1)))

    # 왼쪽에 위치한 톱니바퀴 탐색
    for i in range(number, 1, -1):
        if wheel[i][6] == wheel[i - 1][2]:
            break
        move_wheel.append((i - 1, direction * (-1) ** (number - i + 1)))

    for num, d in move_wheel:
        if d == 1:  # 시계방향
            wheel[num].appendleft(wheel[num].pop())
        else:  # 반시계방향
            wheel[num].append(wheel[num].popleft())

# 점수 계산
score = 0
for i in range(1, 5):
    if wheel[i][0] == '1':
        score += 2 ** (i - 1)

print(score)
