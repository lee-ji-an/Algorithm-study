import sys
from collections import defaultdict
input = sys.stdin.readline

dr = (-1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, 1, 1, 1, 0, -1, -1, -1)

N, M, K = map(int, input().split())

fire_ball = defaultdict(list)
for i in range(M):
    r, c, m, s, d = map(int, input().split())
    fire_ball[(r, c)].append((m, s, d))

for k in range(K):
    move_result = {}
    for pos, f_info in fire_ball.items():
        for info in f_info:
            row, col, mass, speed, direction = pos[0], pos[1], info[0], info[1], info[2]
            mv_row, mv_col = (row + dr[direction] * speed) % N, (col + dc[direction] * speed) % N

            if (mv_row, mv_col) in move_result:
                move_result[(mv_row, mv_col)].append((mass, speed, direction))
            else:
                move_result[(mv_row, mv_col)] = [(mass, speed, direction)]

    fire_ball = defaultdict(list)
    for key, balls in move_result.items():
        row, col = key

        total_mass = 0
        total_speed = 0
        total_dir = 0
        if len(balls) != 1:
            for ball in balls:
                total_mass += ball[0]
                total_speed += ball[1]
                # total_dir += fire_ball[ball][4]
            if all(True if ball[2] % 2 == 0 else False for ball in balls) or \
                    all(True if ball[2] % 2 == 1 else False for ball in balls):
                dir_list = (0, 2, 4, 6)
            else:
                dir_list = (1, 3, 5, 7)

            if int(total_mass / 5) > 0:
                for i in range(4):
                    fire_ball[(row, col)].append((int(total_mass / 5), int(total_speed / len(balls)), dir_list[i]))
        else:
            fire_ball[(row, col)].append((balls[0][0], balls[0][1], balls[0][2]))

ans = 0
for balls in fire_ball.values():
    ans += sum(ball[0] for ball in balls)
print(ans)
