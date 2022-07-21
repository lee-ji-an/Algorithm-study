import sys
n = int(sys.stdin.readline())
l = []
stack = [0 for _ in range(n)]
ans = []
value = 1
ptr = -1
boolean = True
for i in range(n):
    l.append(int(sys.stdin.readline()))
for i in range(n):
    if value <= l[i]:
        for j in range(l[i]-value+1):
            ans.append("+")
            ptr = ptr + 1
            stack[ptr] = value
            value = value + 1
        ans.append("-")
        ptr = ptr - 1
    elif ptr != -1:
        if stack[ptr] == l[i]:
            ans.append("-")
            ptr = ptr - 1
        else:
            print("NO")
            boolean = False
            break
    else:
        print("NO")
        boolean = False
        break
if boolean:
    for j in range(len(ans)):
        print(ans[j])