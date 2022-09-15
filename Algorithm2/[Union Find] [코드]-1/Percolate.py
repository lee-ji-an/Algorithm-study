import random
import statistics
import math

def root(i):
    while i != ids[i]: i = ids[i]
    return i

def connected(p, q):
    return root(p) == root(q)

def union(p, q):
    id1, id2 = root(p), root(q)
    if id1 == id2: return
    if size[id1] <= size[id2]:
        ids[id1] = id2
        size[id2] += size[id1]
    else:
        ids[id2] = id1
        size[id1] += size[id2]

def simulate(n, t):
    global ids, size
    prob = []
    ids = [0] * (n * n + 2)
    size = [1] * (n * n + 2)
    visited = [0] * (n * n + 2)
    for x in range(t):
        cnt = 0
        for j in range(0, n*n+2):
            ids[j] = j
            size[j] = 1
            visited[j] = 0
        for j in range(n):
            ids[j] = n * n
        for j in range(n * (n - 1), n * n):
            ids[j] = n * n + 1
        while True:
            num = random.randrange(0, n*n)
            if visited[num]:
                continue
            visited[num] = 1
            cnt += 1
            if n*(n-1) <= num:
                size[n*n+1] += 1
            elif 0 <= num < n:
                size[n*n] += 1
            if num-n >= 0 and visited[num-n]:
                union(num, num-n)
            if num+n < n*n and visited[num+n]:
                union(num, num+n)
            if num % n != n-1 and visited[num+1]:
                union(num, num+1)
            if num % n != 0 and visited[num-1]:
                union(num, num-1)
            if connected(n*n, n*n+1):
                break
        prob.append(cnt/(n*n))
    mean = statistics.mean(prob)
    stdev = statistics.stdev(prob)
    interval = [mean-1.96*stdev/math.sqrt(t), mean+1.96*stdev/math.sqrt(t)]
    print("mean                    = ", format(mean, ".10f"))
    print("stdev                   = ", format(stdev, ".10f"))
    print("95% confidence interval = [", format(interval[0], ".10f"),format(interval[1], ".10f"), "]")
    return mean, stdev
