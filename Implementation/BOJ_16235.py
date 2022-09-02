#Date : 2022.08.29
#Update : 2022.09.03
#Classification : Implementation
#Author : leejian

import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
A = [0] * 11
# 현재 양분
earth = [[5] * N for _ in range(N)]
# 나무 나이, 수
tree = [[[] for _ in range(N)] for _ in range(N)]   ## 배열 만드는 것 익히기
cnt = 0
dr = [1, -1, 0, 0, 1, -1, 1, -1]
dc = [0, 0, 1, -1, 1, 1, -1, -1]
def spring():
    global plus
    for r in range(N):
        for c in range(N):
            if len(tree[r][c]) <= 0:
                continue
            for l in range(len(tree[r][c])-1, -1, -1):
                energy = earth[r][c] - tree[r][c][l]
                if energy < 0:
                    summer(r, c, l)
                    tree[r][c] = tree[r][c][l + 1:]
                    break
                else:
                    earth[r][c] = energy
                    tree[r][c][l] += 1
                    if tree[r][c][l] % 5 == 0:  # 죽기 전에 넣어버린다
                        plus.append((r, c))


def summer(row, col, l):
    for x in range(0, l + 1):   ## 고생했던 부분
        earth[row][col] += tree[row][col][x] // 2


def fall():
    for r, c in plus:
        for x in range(8):
            mr = r + dr[x]
            mc = c + dc[x]
            if 0 <= mr < N and 0 <= mc < N:
                tree[mr][mc].append(1)


def winter():
    for r in range(N):
        for c in range(N):
            earth[r][c] += A[r][c]


for i in range(0, N):
    A[i] = list(map(int, input().split()))
for i in range(0, M):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)

for i in range(K):
    plus = []
    spring()
    fall()
    winter()

for r in range(N):
    for c in range(N):
        if len(tree[r][c]) > 0:
            cnt += len(tree[r][c])
print(cnt)