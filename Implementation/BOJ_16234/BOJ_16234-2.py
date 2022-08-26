#Date : 2022.08.26
#Update : 2022.08.26
#Classification : Implementation - bfs / pypy3 o, python3 o
#Author : leejian
import sys
from collections import deque

input = sys.stdin.readline
n, l, r = map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int, input().split())))
top = -1
cnt = 0
stack = [0] * (n*n)
dirr = [-1, 1, 0, 0]
dirc = [0, 0, -1, 1]
def dfs(row, col):
    queue = deque()
    loc = [[0]*n for _ in range(n)]
    s = 0
    queue.append([row, col])
    visited[row][col] = 1
    loc[row][col] = 1
    s += A[row][col]
    pos = [(row, col)]
    while queue:
        v = queue.popleft()
        row, col = v[0], v[1]
        for x in range(4):
            mr = row + dirr[x]
            mc = col + dirc[x]
            if 0 <= mr < n and 0 <= mc < n and not visited[mr][mc]:
                if l <= abs(A[mr][mc]-A[row][col]) <= r:
                    queue.append([mr, mc])
                    visited[mr][mc] = 1 ### 방문 표시를 스택에 넣을 때 해야함
                    pos.append((mr, mc))
                    s += A[mr][mc]
    if len(pos) > 1:
        avg = int(s/len(pos))
        for x in range(len(pos)):
            A[pos[x][0]][pos[x][1]] = avg
        return 1
    print(pos)
    return 0

def check(row, col):
    for x in range(4):
        mr, mc = row + dirr[x], col + dirc[x]
        if 0 <= mr < n and 0 <= mc < n:
            if l <= abs(A[mr][mc]-A[row][col]) <= r:
                return 1
    return 0

flag = True
while flag:
    visited = [[0] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                if dfs(i, j):
                    flag = True
    cnt += 1

print(cnt-1)


