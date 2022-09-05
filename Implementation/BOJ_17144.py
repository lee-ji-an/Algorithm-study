#Date : 2022.09.05
#Update : 2022.09.05
#Classification : Implementation (pypy3 - o, python3 - x)
#Author : leejian

import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
room = []
cleanerLoc = []
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
total = 0
cleaner_row1 = 0
cleaner_row2 = 0
def dust():
    sub_room = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if room[r][c] <= 0:
                continue
            amount = room[r][c] // 5
            neighbor = 0
            for x in range(4):
                dust_mr = r + dr[x]
                dust_mc = c + dc[x]
                if 0 <= dust_mr < R and 0 <= dust_mc < C:
                    if dust_mr == cleaner_row1 and dust_mc == 0:
                        continue
                    if dust_mr == cleaner_row2 and dust_mc == 0:
                        continue
                    sub_room[dust_mr][dust_mc] += amount
                    neighbor += 1
            sub_room[r][c] -= amount * neighbor
    for r in range(R):
        for c in range(C):
            room[r][c] += sub_room[r][c]
def cycle(row1, row2):
    #top cycle
    #left
    for r in range(row1-2, -1, -1):
        room[r+1][0] = room[r][0]
    #top
    for c in range(1, C):
        room[0][c-1] = room[0][c]
    #right
    for r in range(1, row1+1):
        room[r-1][C-1] = room[r][C-1]
    #bottom
    for c in range(C-2, 0, -1):
        room[row1][c+1] = room[row1][c]
    room[row1][1] = 0

    # bottom cycle
    # left
    for r in range(row2+2, R):
        room[r-1][0] = room[r][0]
    # bottom
    for c in range(1, C):
        room[R-1][c-1] = room[R-1][c]
    # right
    for r in range(R-2, row2-1, -1):
        room[r+1][C-1] = room[r][C-1]
    # top
    for c in range(C - 2, 0, -1):
        room[row2][c + 1] = room[row2][c]
    room[row2][1] = 0

for i in range(R):
    room.append(list(map(int, input().split())))
    if room[i][0] == -1:
        if not cleaner_row1:
            cleaner_row1 = i
        else:
            cleaner_row2 = i
for i in range(T):
    dust()
    cycle(cleaner_row1, cleaner_row2)

for i in range(R):
    for j in range(C):
        if room[i][j] == -1:
            continue
        if room[i][j] > 0:
            total += room[i][j]

print(total)