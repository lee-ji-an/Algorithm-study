import sys
input = sys.stdin.readline

HOME, CHICKEN = 1, 2
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

N, M = map(int, input().split())
board = []
chicken = []
home = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == HOME:
            home.append((i, j))
        elif row[j] == CHICKEN:
            chicken.append((i, j))
    board.append(row)


def combinations(start, depth):
    global min_dist
    if depth == M:
        # 치킨집을 M 개 모두 골랐을 때 도시의 치킨 거리의 최솟값 구함
        chicken_distance = 0
        for h in range(len(home)):
            sub_distance = float('inf')
            for shop in picked_shop:
                sub_distance = min(sub_distance, distance_table[h][shop])
            chicken_distance += sub_distance
        min_dist = min(chicken_distance, min_dist)
        return

    for i in range(start, len(chicken)):
        picked_shop[depth] = i
        combinations(i + 1, depth + 1)


# 집 - 치킨집 의 거리를 모두 구해 2차원 배열에 저장
def calcul_dist():
    for i in range(len(home)):
        for j in range(len(chicken)):
            distance_table[i][j] = abs(home[i][0] - chicken[j][0]) + abs(home[i][1] - chicken[j][1])


min_dist = float('inf')
picked_shop = [0] * M
distance_table = [[0] * len(chicken) for _ in range(len(home))]

calcul_dist()
combinations(0, 0)

print(min_dist)
