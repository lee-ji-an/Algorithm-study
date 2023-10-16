import sys
input = sys.stdin.readline

dr = (0, -1, 1, 0, 0)
dc = (0, 0, 0, -1, 1)

N, M, K = map(int, input().split())
board = []
directions = [[]]
shark_info = [[0] * 3 for i in range(M + 1)]
smell_board = [[(-1, -1)] * N for _ in range(N)]
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] > 0:
            shark_info[row[j]][0], shark_info[row[j]][1] = i, j
    board.append(row)

cur_dir = list(map(int, input().split()))
for i in range(0, M):
    shark_info[i + 1][2] = cur_dir[i]

for i in range(M):
    one_shark_direction = [[]]
    for j in range(4):
        one_shark_direction.append(list(map(int, input().split())))
    directions.append(one_shark_direction)


def move():
    alive_shark = M
    for time in range(1000):
        for m in range(1, M + 1):
            if shark_info[m][0] == -1:
                continue
            row, col = shark_info[m][0], shark_info[m][1]
            smell_board[row][col] = (m, time)

        move_result = [[0] * 3 for _ in range(M + 1)]
        for m in range(1, M + 1):
            if shark_info[m][0] == -1:
                continue
            row, col, direction = shark_info[m][0], shark_info[m][1], shark_info[m][2]
            dest_row, dest_col, dest_dir = -1, -1, -1

            for direct in directions[m][direction]:
                mv_row, mv_col = row + dr[direct], col + dc[direct]
                if not(0 <= mv_row < N) or not(0 <= mv_col < N):
                    continue
                if smell_board[mv_row][mv_col][0] == -1 or time - smell_board[mv_row][mv_col][1] >= K:
                    dest_row, dest_col, dest_dir = mv_row, mv_col, direct
                    break
            # 냄새가 없는 칸이 없을 때 -> 내 냄새가 있는 곳 탐색
            if dest_row == -1:
                for direct in directions[m][direction]:
                    mv_row, mv_col = row + dr[direct], col + dc[direct]
                    if not (0 <= mv_row < N) or not (0 <= mv_col < N):
                        continue
                    if smell_board[mv_row][mv_col][0] == m:
                        dest_row, dest_col, dest_dir = mv_row, mv_col, direct
                        break

            move_result[m][0], move_result[m][1], move_result[m][2] = dest_row, dest_col, dest_dir

        visited = set()
        for m in range(1, M + 1):
            if shark_info[m][0] == -1:
                continue
            row, col, direction = move_result[m][0], move_result[m][1], move_result[m][2]
            if (row, col) in visited:
                shark_info[m][0], shark_info[m][1], shark_info[m][2] = -1, -1, -1
                alive_shark -= 1
            else:
                shark_info[m][0], shark_info[m][1], shark_info[m][2] = row, col, direction
                visited.add((row, col))
        if alive_shark <= 1:
            return time + 1
    return -1


print(move())
