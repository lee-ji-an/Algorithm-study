#Date : 2022.08.12
#Update : 2022.08.12
#Classification : Dynamic Prigramming
#Author : leejian

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n+1)]
for i in range(1, n + 1):
    w, v = map(int, input().split())
    for j in range(1, k + 1):
        if w > j:
            dp[i][j] = dp[i-1][j]
            continue
        dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])
print(dp[n][k])