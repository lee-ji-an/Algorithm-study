#Date : 2022.08.01
#Update : 2022.08.01
#Classification : Brute-Force / recursion dfs
#Author : leejian 시간초과

# 중복 주의..
# 조합에서는 start가 있어야 함
import sys
import copy
def dfs(num, start, b):
    global case
    if num == n:
        case = case + 1
        return
    i = start
    # for i in range(start, n):
    for j  in range(n):
        if b[i][j] == 0:
            b2 = copy.deepcopy(b)
            board2_set(i, j, 1, b2)
            dfs(num + 1, start+1, b2)

def board2_set(row, col, val, board2):
    # print(board2, "*")
    # board2[row][col] = val
    for k in range(0, n):
        board2[k][col] = val
        board2[row][k] = val
        if row - k >= 0:
            if col - k >= 0:
                board2[row - k][col - k] = val
            if col + k < n:
                board2[row - k][col + k] = val
        if row + k < n:
            if col - k >= 0:
                board2[row + k][col - k] = val
            if col + k < n:
                board2[row + k][col + k] = val

n = int(sys.stdin.readline())
board = [[0]*n for _ in range(n)]
case = 0
dfs(0, 0, board)
print(case)