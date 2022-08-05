#Date : 2022.08.02
#Update : 2022.08.02
#Classification : Brute-Force / recursion dfs
#Author : leejian

import sys
def dfs(num):   #num : queen 의 갯수
    global case
    if num == n:
        case = case + 1
        return
    for i in range(n):
        if check(num, i):   # 다른 퀸을 공격할 수 있는지 체크
            queen[num] = i  # 공격 불가능하면 queen을 배치
            dfs(num+1)

def check(row, col): # 공격 가능하면 return 0, 불가능하면 return 1
    for j in range(row):
        if queen[j] == col or abs(col-queen[j]) == row-j:
            return 0
    return 1

n = int(sys.stdin.readline())
queen = [-1] * n
case = 0
dfs(0)
print(case)