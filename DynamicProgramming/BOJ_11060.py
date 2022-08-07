import sys
input = sys.stdin.readline

def dp(n):
    for i in range(n):
        if ans[i] != N:
            for j in range(1, maze[i]+1):
                if i + j < n:
                    ans[i + j] = min(ans[i] + 1, ans[i + j])
        # print(ans)
N = int(input())
maze = list(map(int, input().split()))
ans = [N]*N
ans[0] = 0
dp(N)
if ans[N-1] == N:
    print(-1)
else:
    print(ans[N-1])