#Date : 2022.08.10
#Update : 2022.08.10
#Classification : Dynamic Programming
#Author : leejian

import sys
input = sys.stdin.readline
n = int(input())
dp = [[0] * 3 for _ in range(10001)]

dp[1][0], dp[1][1], dp[1][2] = 1, 0, 0
dp[2][0], dp[2][1], dp[2][2] = 1, 1, 0
dp[3][0], dp[3][1], dp[3][2] = 2, 0, 1

for i in range(n):
    num = int(input().rstrip())
    for j in range(4, num + 1):
        if dp[num][0] == 0:
            dp[j][0] = dp[j-1][0] + dp[j-1][1] + dp[j-1][2]
            dp[j][1] = dp[j-2][1] + dp[j-2][2]
            dp[j][2] = dp[j-3][2]
    print(dp[num][0] + dp[num][1] + dp[num][2])

# print(n, num)