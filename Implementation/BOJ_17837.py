import sys
from collections import deque
input = sys.stdin.readline
WHITE, RED, BLUE = 0, 1, 2
dr = (0, 0, 0, -1, 1)
dc = (0, 1, -1, 0, 0)
N, K = map(int, input().split())
board = []
pieces = [[deque() for _ in range(N)] for _ in range(N)]
pieces_info = {}

for _ in range(N):
    board.append(list(map(int, input().split())))

for i in range(K):
    row, col, direction = map(int, input().split())
    pieces[row - 1][col - 1].append(i)
    pieces_info[i] = [row - 1, col - 1, direction]


def back(direction):
    return direction + 1 if direction % 2 == 1 else direction - 1


def do_white(row, col, mv_row, mv_col, number):
    temp = []
    while pieces[row][col]:
        num = pieces[row][col].pop()
        temp.append(num)
        if num == number:
            break
    for i in range(len(temp) - 1, -1, -1):
        pieces[mv_row][mv_col].append(temp[i])
        pieces_info[temp[i]][0], pieces_info[temp[i]][1] = mv_row, mv_col


def do_red(row, col, mv_row, mv_col, number):
    while pieces[row][col]:
        num = pieces[row][col].pop()
        pieces_info[num][0], pieces_info[num][1] = mv_row, mv_col
        pieces[mv_row][mv_col].append(num)

        if number == num:
            return


def play():
    for i in range(1000):
        for p in range(K):
            r, c, direction = pieces_info[p][0], pieces_info[p][1], pieces_info[p][2]
            if not pieces[r][c]:
                continue
            mv_row, mv_col = r + dr[direction], c + dc[direction]
            if not(0 <= mv_row < N) or not(0 <= mv_col < N) or board[mv_row][mv_col] == BLUE:
                back_dir = back(direction)
                pieces_info[p][2] = back_dir
                mv_row, mv_col = r + dr[back_dir], c + dc[back_dir]
                if not (0 <= mv_row < N) or not (0 <= mv_col < N) or board[mv_row][mv_col] == BLUE:
                    continue
                if board[mv_row][mv_col] == RED:
                    do_red(r, c, mv_row, mv_col, p)
                elif board[mv_row][mv_col] == WHITE:
                    do_white(r, c, mv_row, mv_col, p)

            elif board[mv_row][mv_col] == WHITE:
                do_white(r, c, mv_row, mv_col, p)
            elif board[mv_row][mv_col] == RED:
                do_red(r, c, mv_row, mv_col, p)

            if len(pieces[mv_row][mv_col]) >= 4:
                return i + 1

    return -1


print(play())
