import sys


def solution(maxSize, actions):
    from collections import defaultdict, deque
    ans = 0
    recent = deque()
    back = [0] * 100001
    front = [0] * 100001
    back_ptr, front_ptr = -1, -1

    for action in actions:
        if action == "B":
            if len(back) > 0:
                if recent:
                    front_ptr += 1
                    front[front_ptr] = recent[0]
                    if back_ptr >= 0:
                        recent.appendleft(back[back_ptr])
                        back_ptr -= 1
        elif action == "F":
            if len(front) > 0:
                if recent:
                    back_ptr += 1
                    back[back_ptr] = recent[0]
                    # back.append(recent[0])
                    if front_ptr >= 0:
                        recent.appendleft(front[front_ptr])
                        front_ptr -= 1
        else:
            front = [0] * 100001
            front_ptr = -1
            if recent:
                back_ptr += 1
                back[back_ptr] = recent[0]
            # back.append(action)
            # if action in recent:
            #     recent.remove(action)
            recent.appendleft(action)
            # if len(recent) > maxSize:
            #     recent.pop()
        # print(action,recent, front_ptr)#, back[0:back_ptr], front[0:front_ptr])
    ans = []
    # print(recent)
    for i in range(len(recent)):
        # print(recent[i])
        if recent[i] not in ans:
            ans.append(recent[i])
        if len(ans) == maxSize:
            break

    return ans

def solution2(maxSize, actions):
    from collections import defaultdict, deque
    ans = 0
    recent = deque()
    back = []
    front = []
    # back_ptr, front_ptr = -1

    for action in actions:
        if action == "B":
            if len(back) > 0:
                front.append(recent[0])
                recent.appendleft(back.pop())
        elif action == "F":
            if len(front) > 0:
                back.append(recent[0])
                recent.appendleft(front.pop())
        else:
            front.clear()
            if recent:
                back.append(recent[0])
            # back.append(action)
            # if action in recent:
            #     recent.remove(action)
            recent.appendleft(action)
            # if len(recent) > maxSize:
            #     recent.pop()
        # print(action, recent, back, front)
    ans = []
    # print(recent)
    for i in range(len(recent)):
        # print(recent[i])
        if recent[i] not in ans:
            ans.append(recent[i])
        if len(ans) == maxSize:
            break

    return ans

print(solution(3, ["1", "2", "3", "4", "3"]))
print(solution(1, ["B", "F"]))
print(solution(3, ["1", "3", "2", "B", "4", "F"]))
print(solution(3, ["1", "2", "B", "F"]))

