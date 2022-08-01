#Date : 2022.08.01
#Update : 2022.08.01
#Classification : Brute-Force / dfs
#Author : leejian

import sys
input = sys.stdin.readline
def dfs(idx, e):
    global maxE
    if idx == n-2:
        maxE = max(e, maxE)
        return
    for i in range(1, n-1):
        if check[i]:
            check[i] = 0
            for j in range(i, -1, -1):
                if check[j] == 1:
                    left = j
                    break
            for j in range (i+1, n):
                if check[j] == 1:
                    right = j
                    break
            # print(wlist[i], wlist[left], wlist[right])
            dfs(idx + 1, e + wlist[left] * wlist[right])
            check[i] = 1

n = int(input())
wlist = list(map(int, input().split()))

# print(n)
# print(wlist)
check = [1] * n
maxE = 0
dfs(0, 0)
print(maxE)