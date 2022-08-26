#Date : 2022.08.26
#Update : 2022.08.26
#Classification : Implementation - dfs / pypy3 o, python3 시간초과
#Author : leejian

import sys
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
    global top
    loc = [[0]*n for _ in range(n)]
    top = -1
    s = 0
    num = 0
    push([row, col])
    visited[row][col] = 1
    loc[row][col] = 1
    while top != -1:
        v = pop()
        row, col = v[0], v[1]
        s += A[row][col]
        num += 1
        for x in range(4):
            mr = row + dirr[x]
            mc = col + dirc[x]
            if 0 <= mr < n and 0 <= mc < n and not visited[mr][mc]:
                if door[row][col][x]:
                    push([mr, mc])
                    visited[mr][mc] = 1 ### 방문 표시를 스택에 넣을 때 해야함
                    loc[mr][mc] = 1
    avg = int(s/num)
    for x in range(n):
        for y in range(n):
            if loc[x][y] == 1:
               A[x][y] = avg
    if num > 1:
        return True
    else:
        return False

def push(item):
    global top
    top = top + 1
    stack[top] = item
def pop():
    global top
    top = top - 1
    return stack[top+1]

flag = True
while flag:
    door = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if 0 <= i+1 < n and 0 <= j < n:
                if l <= abs(A[i+1][j] - A[i][j]) <= r:
                    door[i][j][1] = 1
                    door[i+1][j][0] = 1
            if 0 <= i < n and 0 <= j+1 < n:
                if l <= abs(A[i][j] - A[i][j+1]) <= r:
                    door[i][j][3] = 1
                    door[i][j+1][2] = 1
    # print(door)
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                if door[i][j][0] or door[i][j][1] or door[i][j][2] or door[i][j][3]:
                    if dfs(i, j):
                        flag = True
    cnt += 1

print(cnt-1)


