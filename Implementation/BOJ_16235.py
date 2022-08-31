import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
A = [0] * 11
# 현재 양분
earth = [[5] * N for _ in range(N)]
# 나무 나이, 수
tree = [[[] for _ in range(N)] for _ in range(N)]   ## 배열 만드는 것 익히기
cnt = 0

def spring():
    global plus
    for r in range(N):
        for c in range(N):
            if len(tree[r][c]) <= 0:
                continue
            flag = False
            for l in range(len(tree[r][c])-1, -1, -1):
                energy = earth[r][c] - tree[r][c][l]
                if energy < 0:
                    flag = True
                    break
                earth[r][c] = energy
                tree[r][c][l] += 1
                if tree[r][c][l] % 5 == 0:  # 죽기 전에 넣어버린다
                    plus.append((r, c))
            if flag:
                summer(r, c, l)
                tree[r][c] = tree[r][c][l+1 : ]

def summer(row, col, l):
    for _ in range(0, l + 1):
        earth[row][col] += tree[row][col][l] // 2


def fall():
    for r, c in plus:
        left, right, top, bottom = False, False, False, False   ##주의
        # print("row, col : ",r, c)
        if c+1 < N:
            tree[r][c+1].append(1)
            right = True
        if c-1 >= 0:
            tree[r][c-1].append(1)
            left = True
        if r+1 < N:
            tree[r+1][c].append(1)
            bottom = True
        if r-1 >= 0:
            tree[r-1][c].append(1)
            top = True
        if right and top:
            tree[r-1][c+1].append(1)
        if right and bottom:
            tree[r+1][c+1].append(1)
        if left and top:
            tree[r-1][c-1].append(1)
        if left and bottom:
            tree[r+1][c-1].append(1)

def winter():
    for r in range(N):
        for c in range(N):
            earth[r][c] += A[r][c]


for i in range(0, N):
    A[i] = list(map(int, input().split()))
for i in range(0, M):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)

for i in range(K):
    plus = []
    spring()
    fall()
    winter()
# for i in range(N):
#     print(tree[i])
# for i in range(N):
#     print(earth[i])

for r in range(N):
    for c in range(N):
        if len(tree[r][c]) > 0:
            cnt += len(tree[r][c])
print(cnt)