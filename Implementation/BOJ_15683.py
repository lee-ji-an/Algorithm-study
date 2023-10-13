import sys
input = sys.stdin.readline

WALL = 6
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

N, M = map(int, input().split())
cctv = []
# CCTV 번호에 따라 감시할 수 있는 방향
direction = [0,
             [[0], [1], [2], [3]],
             [(0, 1), (2, 3)], [(0, 3), (0, 2), (1, 2), (1, 3)],
             [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)],
             [(0, 1, 2, 3)]
             ]

board = []
wall = 0
for r in range(N):
    row = list(map(int, input().split()))
    for c in range(M):
        if 1 <= row[c] <= 5:
            cctv.append((r, c))
        if row[c] == 6:
            wall += 1
    board.append(row)


def dfs(idx, size, board):
    global ans
    if idx >= len(cctv):
        ans = max(ans, size)
        return

    row, col = cctv[idx]
    number = board[row][col]

    for direct in direction[number]:
        new_board = [r[:] for r in board]
        cnt = 0
        for d in direct:
            # d 방향으로 cctv 탐색
            for i in range(1, max(N, M)):
                mv_row, mv_col = row + dr[d] * i, col + dc[d] * i
                if not (0 <= mv_row < N) or not (0 <= mv_col < M):
                    break
                if new_board[mv_row][mv_col] == 6:
                    break
                # CCTV가 감시 가능한 구역 중 아직 검사되지 않은 칸이 있으면 마킹 & cnt 증가
                if new_board[mv_row][mv_col] != -1 and not(1 <= new_board[mv_row][mv_col] <= 5):
                    new_board[mv_row][mv_col] = -1
                    cnt += 1
        dfs(idx + 1, size + cnt, new_board)


ans = float('-inf')
dfs(0, 0, board)
print(N * M - ans - wall - len(cctv))
