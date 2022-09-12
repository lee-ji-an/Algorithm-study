#Date : 2022.09.07
#Update : 2022.09.11
#Classification : Implementation(python3 - o)
#Author : leejian

import sys
input = sys.stdin.readline
man = -1
cnt = 0
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, 1, -1]
def catch(loc, size):
    for r in range(R):
        if sea[r][loc]:
            size += sea[r][loc][2]
            sea[r][loc] = 0
            break
    return size

def move():
    sub_sea = [[[] for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if sea[r][c]:
                speed, dir, z = sea[r][c][0], sea[r][c][1], sea[r][c][2]
                mr, mc, dir = get_loc(r, c, speed, dir)
                sub_sea[mr][mc].append((speed, dir, z))
    for r in range(R):
        for c in range(C):
            if len(sub_sea[r][c]) > 1:
                max_idx = 0
                for x in range(1, len(sub_sea[r][c])):
                    if sub_sea[r][c][max_idx][2] < sub_sea[r][c][x][2]:
                        max_idx = x
                sea[r][c] = sub_sea[r][c][max_idx]
            elif len(sub_sea[r][c]) == 1:
                sea[r][c] = sub_sea[r][c][0]
            else:
                sea[r][c] = 0

def get_loc(row, col, s, d):
    if d == 1 or d == 2:
        if row == 0 or row == R-1 or d == 2:
            new_r = (row + s)%(2*R - 2)
        elif d == 1:
            new_r = (2 * R - row - 2 + s)%(2*R - 2)
        if new_r <= R-2:
            return new_r, col, 2
        else:
            return 2*R-2-new_r, col, 1
    if d == 3 or d == 4:
        if col == 0 or col == C-1 or d == 3:
            new_c = (col + s)%(2*C - 2)
        elif d == 4:
            new_c = (2*C-col-2+s)%(2*C - 2)
        if new_c <= C-2:
            return row, new_c, 3
        else:
            return row, 2*C-2-new_c, 4


R, C, M = map(int, input().split())
sea = [[0 for _ in range(C)] for _ in range(R)]
for i in range(M):
    row, col, S, D, Z = map(int, input().split())
    sea[row-1][col-1] = (S, D, Z)
for i in range(C):
    cnt = catch(i, cnt)
    move()
    # print(sea)

print(cnt)
