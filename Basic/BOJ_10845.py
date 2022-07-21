# stack 풀었던 걸 경험삼아 한 번에 정답!!

import sys
n = int(sys.stdin.readline())
queue = [0 for i in range(n)]
front = -1
end = -1
for i in range(n):
    command = sys.stdin.readline().strip()
    if command.startswith("push"):
        end = end + 1
        queue[end] = int(command[5:])
    elif command == "pop":
        if front == end:
            print("-1")
        else:
            front = front + 1
            print(queue[front])
    elif command == "size":
        print(end-front)
    elif command == "empty":
        if front == end:
            print("1")
        else:
            print("0")
    elif command == "front":
        if front == end:
            print("-1")
        else:
            print(queue[front+1])
    else:
        if front == end:
            print("-1")
        else:
            print(queue[end])

