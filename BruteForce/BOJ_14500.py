#Date : 2022.07.31
#Update : 2022.07.31
#Classification : Brute-Force / recursion
#Author : leejian

import sys
input = sys.stdin.readline
num_list = []
n, m = map(int, input().split())
# for i in range(n):
#     num_list.append(list(map(int, input().split())))

num_list = [list(map(int, input().split())) for _ in range(n)]

def dfs(idx, row, col, sum):
    global max_val, ans
    if ans >= sum + max_val * (4-idx):      # 시간 줄이기에 중요
        return
    if idx == 4:
        ans = max(sum, ans)
        return
    else:
        for i in range(4):
            move_r = row + dir_r[i]
            move_c = col + dir_c[i]
            if 0 <= move_r < n and 0 <= move_c < m and not visited[move_r][move_c]:
                visited[move_r][move_c] = 1
                if idx == 2:    # ㅗ ㅜ ㅓ ㅏ 모양을 탐색하기 위한 구문
                    dfs(idx + 1, row, col, sum + num_list[move_r][move_c])
                dfs(idx + 1, move_r, move_c, sum + num_list[move_r][move_c])
                visited[move_r][move_c] = 0

sum = 0
max_val = max(map(max, num_list))
ans = 0
visited = [([0] * m) for _ in range(n)]
dir_r = [-1, 0, 1, 0]
dir_c = [0, -1, 0, 1]
for r in range(n):
    for c in range(m):
        visited[r][c] = 1
        dfs(1, r, c, num_list[r][c])
        visited[r][c] = 0
print(ans)