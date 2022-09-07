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
                s, d, z = sea[r][c][0], sea[r][c][1], sea[r][c][2]
                mr = r
                mc = c
                for x in range(s):
                    mr += dr[d]
                    mc += dc[d]
                    if 0 <= mr < R and 0 <= mc < C:
                        continue
                    else:
                        if d == 1:
                            d = 2
                        elif d == 2:
                            d = 1
                        elif d == 3:
                            d = 4
                        else:
                            d = 3
                        mr = mr + dr[d]*2
                        mc = mc + dc[d]*2
                sub_sea[mr][mc].append((s, d, z))
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



R, C, M = map(int, input().split())
sea = [[0 for _ in range(C)] for _ in range(R)]
for i in range(M):
    row, col, S, D, Z = map(int, input().split())
    sea[row-1][col-1] = (S, D, Z)
for i in range(C):
    cnt = catch(i, cnt)
    move()

print(cnt)
