#Date : 2022.08.09
#Update : 2022.08.09
#Classification : Dynamic Programming
#Author : leejian

import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
m = int(input())
dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1
for i in range(n-1):
    if num[i] == num[i+1]:
        dp[i][i+1] = 1
for i in range(2, n):
    for j in range(0, n-i):
        if dp[j+1][j+i-1] == 1 and num[j] == num[j+i]:
            dp[j][j+i] = 1

for i in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])