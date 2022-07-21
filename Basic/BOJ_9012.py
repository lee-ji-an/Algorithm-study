import sys
# ( 가 먼저 나와야 )가 나올 수 있는 게 중요
n = int(sys.stdin.readline())
for i in range(n):
    s = sys.stdin.readline().strip()
    ptr = -1
    for j in range(len(s)):
        if s[j] == "(":
            ptr = ptr + 1
        else:
            ptr = ptr - 1
            if ptr < -1:   ## 실수한 부분
                break
    if ptr == -1:
        print("YES")
    else:
        print("NO")