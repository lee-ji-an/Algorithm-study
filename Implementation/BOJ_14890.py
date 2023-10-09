import sys
input = sys.stdin.readline

N, L = map(int, input().split())

board = []
for n in range(N):
    board.append(list(map(int, input().split())))

visited = [[False] * N for _ in range(N)]

ans = 0

check = []
for r in range(N):
    sub_row_check = []
    prev, cnt = board[r][0], 0
    for c in range(N):
        if prev == board[r][c]:
            cnt += 1
        else:
            sub_row_check.append((prev, cnt))
            prev, cnt = board[r][c], 1
    sub_row_check.append((prev, cnt))
    check.append(sub_row_check)

for c in range(N):
    sub_col_check = []
    prev, cnt = board[0][c], 0
    for r in range(N):
        if prev == board[r][c]:
            cnt += 1
        else:
            sub_col_check.append((prev, cnt))
            prev, cnt = board[r][c], 1
    sub_col_check.append((prev, cnt))
    check.append(sub_col_check)


for r in range(N * 2):
    prev, p_cnt = check[r][0]
    for i in range(1, len(check[r])):
        height, cnt = check[r][i]
        if abs(height - prev) > 1:
            break
        if height > prev:  # 높아졌을 때
            if p_cnt < L:
                break
        else:  # 낮아졌을 때
            if cnt < L:
                break
            cnt -= L

        prev, p_cnt = height, cnt
    else:
        ans += 1

print(ans)
