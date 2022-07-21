import sys
n = int(sys.stdin.readline())
stack = [0 for i in range(n)]
ptr = -1
for i in range(n):
    command = sys.stdin.readline().strip()  # 개행문자도 들어가는 것 주의
    if command.startswith("push"):
        ptr = ptr + 1
        stack[ptr] = int(command[5:])
    elif command == "pop":
        if ptr == -1:
            print(-1)
        else:
            print(stack[ptr])
            ptr = ptr - 1
    elif command == "size":
        print(ptr+1)
    elif command == "empty":
        if ptr == -1:
            print("1")
        else:
            print("0")
    else:
        if ptr == -1:
            print(-1)
        else:
            print(stack[ptr])