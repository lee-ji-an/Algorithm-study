import sys
input = sys.stdin.readline

dr = (0, -1, 0, 1)
dc = (1, 0, -1, 0)

N = int(input())
board = [[True] * 101 for _ in range(101)]
visited = [[False] * 101 for _ in range(101)]


def rotate(dragon, rotate_point):
    sub_dragon = set()
    for r, c in dragon:
        mv_r, mv_c = (c - rotate_point[1]) + rotate_point[0], rotate_point[1] - (r - rotate_point[0])
        sub_dragon.add((mv_r, mv_c))
    return dragon.union(sub_dragon)


for n in range(N):
    C, R, D, G = map(int, input().split())
    dragon = {(R, C)}
    dragon.add((R + dr[D], C + dc[D]))
    rotate_point = (R + dr[D], C + dc[D])

    if G >= 1:
        for g in range(1, G + 1):
            dragon = rotate(dragon, rotate_point)
            # 회전 축을 중심으로 첫 시작 지점인 (R, C) 를 회전시킨 지점이 다음 회전 축이 됨.
            rotate_point = (C - rotate_point[1]) + rotate_point[0], rotate_point[1] - (R - rotate_point[0])

    for row, col in dragon:
        visited[row][col] = True

# 네 꼭짓점을 감싸는 네모를 찾아서 카운트
ans = 0
for r in range(100):
    for c in range(100):
        if all(visited[row][col] for row, col in ((r, c), (r + 1, c), (r, c + 1), (r + 1, c + 1))):
            ans += 1
print(ans)


