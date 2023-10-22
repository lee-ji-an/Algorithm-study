import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
durability = deque(list(map(int, input().split())))
box_robot = deque([False] * (2 * N))

ans = durability[0] + 1
t = 1
k = K
while True:
    box_robot.pop()
    box_robot.appendleft(False)
    box_robot[N - 1] = False
    durability.appendleft(durability.pop())

    for i in range(N-2, -1, -1):
        if box_robot[i]:
            if not box_robot[i + 1] and durability[i + 1] > 0:
                box_robot[i + 1] = True
                box_robot[i] = False
                durability[i + 1] -= 1

                if durability[i + 1] == 0:
                    k -= 1
    box_robot[N - 1] = False

    if k <= 0:
        ans = t
        break

    if durability[0] > 0:
        box_robot[0] = True
        durability[0] -= 1

        if durability[0] == 0:
            k -= 1

    if k <= 0:
        ans = t
        break

    t += 1

print(ans)
