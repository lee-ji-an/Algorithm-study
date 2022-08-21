#Date : 2022.08.17
#Update : 2022.08.17
#Classification : Dynamic Prigramming
#Author : leejian

import sys

input = sys.stdin.readline
n, s, m = map(int, input().split())
v = list(map(int, input().split()))
dp = [[0]*(m+1) for _ in range(n+1)]
dp[0][s] = 1
for i in range(1, n+1):
    s = v[i-1]
    for j in range(m+1):
        if dp[i-1][j] == 1:
            if j+s <= m:
                dp[i][j+s] = 1
            if j-s >= 0:
                dp[i][j-s] = 1
flag = True
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        print(i)
        flag = False
        break
if flag:
    print(-1)