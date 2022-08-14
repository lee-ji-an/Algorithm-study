#Date : 2022.08.14
#Update : 2022.08.14
#Classification : Dynamic Prigramming
#Author : leejian

import sys
input = sys.stdin.readline

t = int(input())
dp = [[0] * 500 for _ in range(500)]
# sum = [[0] * 500 for _ in range(500)]
for i in range(t):
    n = int(input())
    file = list(map(int, input().split()))
    # for j in range(n):
    #     sum[j][j] = file[j]
    # for j in range(1, n):
    #     for k in range(0, n-j):
    #         sum[k][k+j] = sum[k][k+j-1] + sum[k+j][k+j]
    # print(sum)
    for j in range(n):
        dp[j][j] = 0
    for j in range(1, n):
        for k in range(0, n-j):
            min = dp[k+1][k+j]
            for l in range(k, j+k):
                if dp[k][l] + dp[l+1][j+k] < min:
                    min = dp[k][l] + dp[l+1][j+k]
            dp[k][k+j] = min + sum(file[k:k+j+1])
    # print(dp)
    print(dp[0][n-1])

