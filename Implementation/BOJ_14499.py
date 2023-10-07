import sys
input = sys.stdin.readline

dr = (0, 0, 0, -1, 1)
dc = (0, 1, -1, 0, 0)

N, M, X, Y, K = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))
command = list(map(int, input().split()))

dice = [0] * 6
posR, posC = X, Y


def roll(direction):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if direction == 1:  # 동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif direction == 2:  # 서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif direction == 3:  # 북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e
    else:  # 남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b


for c in command:
    if not(0 <= posR + dr[c] < N) or not(0 <= posC + dc[c] < M):
        continue
    roll(c)
    posR, posC = posR + dr[c], posC + dc[c]

    if board[posR][posC] == 0:
        board[posR][posC] = dice[0]
    else:
        dice[0] = board[posR][posC]
        board[posR][posC] = 0

    print(dice[5])
