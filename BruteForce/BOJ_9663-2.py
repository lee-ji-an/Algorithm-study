#Date : 2022.08.02
#Update : 2022.08.02
#Classification : Brute-Force / recursion dfs
#Author : leejian

# 중복 주의..
# 조합에서는 start가 있어야 함
import sys
def dfs(num):
    global case
    if num == n:
        case = case + 1
        return
    for i in range(n):
        if check(num, i):
            queen[num] = i
            dfs(num+1)

def check(row, col):
    for j in range(row):
        if queen[j] == col or abs(col-queen[j]) == row-j:
            return 0
    return 1

n = int(sys.stdin.readline())
queen = [-1] * n
case = 0
dfs(0)
print(case)