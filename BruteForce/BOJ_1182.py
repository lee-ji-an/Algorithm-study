import sys
def dfs(start, depth):  #my code
    global cnt
    for i in range(start, n):
        combi[depth] = l[i]
        sum = 0
        for j in range(0, depth+1):
            sum = sum + combi[j]
        if sum == s:
            cnt = cnt + 1
        dfs(i+1, depth+1)

def dfs2(idx, sum): #answer
    global cnt
    if idx >= n:
        return
    sum = sum + l[idx]
    if sum == s:
        cnt = cnt + 1
    dfs2(idx+1, sum-l[idx])
    dfs2(idx+1, sum)

n, s = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
cnt = 0
combi = [0 for i in range(n)]
dfs(0, 0)
print(cnt)