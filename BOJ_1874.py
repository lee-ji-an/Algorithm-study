import sys
n = int(sys.stdin.readline())
l = []
stack = [0 for _ in range(n)]
value = 1
ptr = -1
for i in range(n):
    l.append(int(sys.stdin.readline()))
for i in range(n):
    if value <= l[i]:
        for j in range(l[i]-value+1):
            print("+")
            ptr = ptr + 1
            stack[ptr] = value
        value = value + (l[i] - value) + 1
        print("-")
        ptr = ptr - 1
    elif ptr != -1:
        if stack[ptr] == value:
            print("-")
            ptr = ptr - 1
    else:
        print("NO")
        break
    print("---")