#Date : 2022.08.01
#Update : 2022.08.01
#Classification : Brute-Force / bfs
#Author : leejian reference (https://chelseashin.tistory.com/79)

import sys
from collections import deque
# dfs로 탐색하면 최소값을 보장할 수 없음  -> bfs로 탐색하면 현재 위치와 가장 가까운 거리부터 탐색하므로 첫 번째로 나온 게 최소 탐색하므로 첫 번째로 나온 게 최소
def bfs(b1_row, b1_col, b2_row, b2_col):
    #check :  공을 몇번 옮겨서 도착할 수 있는지 저장하는 리스트
    check = [[[[-1] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    check[b1_row][b1_col][b2_row][b2_col] = 0
    q = deque([(b1_row, b1_col, b2_row, b2_col)]) # queue에 처음 공의 위치를 insert
    while q:
        b1_row, b1_col, b2_row, b2_col = q.popleft() # queue 에서 pop
        if check[b1_row][b1_col][b2_row][b2_col] >= 10: # 버튼을 10번 이상 눌렀는지 확인
            break
            # break를 return -1 로 바꾸고 밑에 return -1을 제거했을 때 생기는 오류 :
            # 10번 누르기 전에 더이상 탐색할 곳이 없어지면 return할 값이 없음
        for i in range(4):
            b1_mr = b1_row + dir_r[i] # 공의 위치 이동
            b1_mc = b1_col + dir_c[i]
            b2_mr = b2_row + dir_r[i]
            b2_mc = b2_col + dir_c[i]
            if not(0 <= b1_mr < n and 0 <= b1_mc < m) and not(0 <= b2_mr < n and 0 <= b2_mc < m):
                continue # 공 2개가 모두 떨어쟀을 때는 continue
            elif not (0 <= b1_mr < n and 0 <= b1_mc < m):   # 공이 하나만 떨어졌다면 return
                return check[b1_row][b1_col][b2_row][b2_col] + 1
            elif not(0 <= b2_mr < n and 0 <= b2_mc < m):     # 공이 하나만 떨어졌다면 return
                return check[b1_row][b1_col][b2_row][b2_col] + 1
            else: # 공이 2개 모두 떨어지지 않았을 때
                if board[b1_mr][b1_mc] == '#': # 옮긴 곳이 벽이라면 다시 원상 복귀
                    b1_mr -= dir_r[i]
                    b1_mc -= dir_c[i]
                if board[b2_mr][b2_mc] == '#':
                    b2_mr -= dir_r[i]
                    b2_mc -= dir_c[i]
                if check[b1_mr][b1_mc][b2_mr][b2_mc] == -1:
                    # 옮긴 곳에 아직 한 번도 도착한 적이 없을 때 몇 번 만에 도착할 수 있는지 기록
                    # 이미 기록이 된 상태라면 기록할 필요가 x -> 최초로 기록한 숫자가 최소이기 때문
                    check[b1_mr][b1_mc][b2_mr][b2_mc] = check[b1_row][b1_col][b2_row][b2_col] + 1
                    q.append((b1_mr, b1_mc, b2_mr, b2_mc))
    return -1
input = sys.stdin.readline
n, m = map(int, input().split())
board = []
ball_pos = []
flag = True
for i in range(n):
    board.append(list(input().rstrip()))
    # 문자열을 입력받기 때문에 '\n' 제거하기 위해 strip 해서 넣음
    for j in range(m):
        if board[i][j] == 'o': # 공의위치 기록
            ball_pos.append([i, j])

dir_r = [-1, 0, 1, 0]
dir_c = [0, 1, 0, -1]
print(bfs(ball_pos[0][0], ball_pos[0][1], ball_pos[1][0], ball_pos[1][1]))
