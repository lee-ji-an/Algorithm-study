#Date : 2022.08.06
#Update : 2022.08.06
#Classification : Dynamic Programming
#Author : leejian

import sys
input = sys.stdin.readline

def dp(n, m):
    for i in range(1, n+1):
        for j in range(1, m+1):
            maze[i][j] = max(maze[i-1][j], maze[i][j-1], maze[i-1][j-1]) + maze[i][j]

N, M = map(int, input().split(" "))
maze = [[0] * (M+1) for _ in range(N+1)]
for i in range(1, N+1):
    temp = list(map(int, input().split(" ")))
    for j in range(1, M+1):
        maze[i][j] = temp[j-1]

dp(N, M)
print(maze[N][M])