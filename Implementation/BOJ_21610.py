import sys
input = sys.stdin.readline

dr = (0, 0, -1, -1, -1, 0, 1, 1, 1)
dc = (0, -1, -1, 0, 1, 1, 1, 0, -1)

N, M = map(int, input().split())

board = []
command = []
cloud = set()
start_pos = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

for _ in range(N):
    board.append(list(map(int, input().split())))
for _ in range(M):
    command.append(tuple(map(int, input().split())))


def move(direction, distance):
    new_cloud = set()
    dir_r, dir_c = dr[direction], dc[direction]
    for row, col in cloud:
        new_cloud.add(((row + dir_r * distance) % N, (col + dir_c * distance) % N))

    return new_cloud


def raining_and_magic(cloud):
    for row, col in cloud:
        board[row][col] += 1

    result = []
    diag = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    for row, col in cloud:
        cnt = 0
        for i in range(4):
            mv_row, mv_col = row + diag[i][0], col + diag[i][1]
            if not(0 <= mv_row < N) or not(0 <= mv_col < N):
                continue
            if board[mv_row][mv_col] > 0:
                cnt += 1
        result.append((row, col, cnt))

    for row, col, cnt in result:
        board[row][col] += cnt


for row, col in start_pos:
    cloud.add((row, col))

for direction, distance in command:
    cloud = move(direction, distance)

    raining_and_magic(cloud)

    new_cloud = set()
    for row in range(N):
        for col in range(N):
            if board[row][col] >= 2 and (row, col) not in cloud:
                new_cloud.add((row, col))
    for row, col in new_cloud:
        board[row][col] -= 2
    cloud = new_cloud

print(sum(sum(r)for r in board))
