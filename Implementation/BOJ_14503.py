import sys
input = sys.stdin.readline

dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)

N, M = map(int, input().split())
posR, posC, direction = map(int, input().split())
if direction % 2 == 1:
    direction = (direction + 2) % 4

board = []
for i in range(N):
    board.append(list(map(int, input().split())))

visited = [[False] * M for _ in range(N)]
ans = 0

while True:
    if not visited[posR][posC]:
        visited[posR][posC] = True
        ans += 1

    for d in range(1, 5):
        new_dir = (direction + d) % 4
        new_posR, new_posC = posR + dr[new_dir], posC + dc[new_dir]

        # 주변에 청소되지 않은 빈 칸이 있을 때
        if board[new_posR][new_posC] == 0 and not visited[new_posR][new_posC]:
            posR, posC, direction = new_posR, new_posC, new_dir
            break

    # 주변에 청소되지 않은 빈 칸이 없는 경우
    else:
        back_dir = (direction + 2) % 4

        # 후진이 가능한지 검사
        if board[posR + dr[back_dir]][posC + dc[back_dir]] == 0:
            posR, posC = posR + dr[back_dir], posC + dc[back_dir]
        else:
            break


print(ans)
