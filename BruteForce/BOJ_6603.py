import sys

def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(combi[i], end=" ")
        print()
        return
    for i in range(start, len(s)):
        combi[depth] = s[i]
        dfs(i+1, depth+1)
combi = [0 for i in range(13)]
n = [7, 1, 2, 3, 4, 5, 6, 7]
while True:
    n = list(map(int, sys.stdin.readline().split()))
    s = n[1:]
    if n[0] == 0:
        break
    dfs(0,0)
    print()