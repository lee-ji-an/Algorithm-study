import random
ids = []
size = []   # size[i]: size of tree rooted at i

def root(r1, c1):
    while r1*5+c1 != ids[r1][c1]:  = ids[r1][c1]
    return i

def connected(p, q):
    return root(p) == root(q)

def union(r1, c1, r2, c2):
    id1r, id1c = root(ids[r1][c1])
    id2r, id2c = root(ids[r2][c2])
    if id1r == id2r and id1c == id2c: return
    if size[id1r][id1c] <= size[id2r][id2c]:
        ids[id1r][id1c] = ids[]
        size[id2] += size[id1]
    else:
        ids[id2] = id1
        size[id1] += size[id2]
N = int(input())
ids = [[0 for y in range(N)] for x in range(N)]
size = [[1 for y in range(N)] for x in range(N)]
size.append([N+1, N+1])
ids.append([N*N, N*N+1])
for i in range(N):
    for j in range(N):
        ids[i][j] = i*5+j
for i in range(N):
    ids[0][i] = N*N
    ids[N-1][i] = N*N+1
print(size)
print(ids)
while True:
    r = random.randrange(0, 5)
    c = random.randrange(0, 5)
    union(ids[r][c], ids[r-1][c])
    union(ids[r][c], ids[r+1][c])

# for idx in range(N):
#     ids.append(idx)
#     size.append(1)
