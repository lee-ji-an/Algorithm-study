# Date : 2023.01.07
# Update : 2023.01.07
# Classification : Brute-Force / permutation
# Author : leejian
# 1차 알고리즘 - 시간초과

import sys

def inequality(s):
    if s[0] == '<':
        myAppend(8)
        myAppend(9)
        left = 9
    else:
        myAppend(9)
        myAppend(8)
        left = 8
    myAppend(7)
    right = 7
    idx = 1
    while True:
        if idx == n:
            break
        if s[idx] == '>':
            if left > right:
                left = right
            else:
                myPop(right)
                for i in range(right - 1, -1, -1):
                    if visited[i] == 1:
                        myAppend(i)
                        right = i
                    break
                continue
        else:
            if left < right:
                left = right
            else:
                myPop(right)
                for i in range(left - 1, -1, -1):
                    if visited[i] == 1:
                        nextR = i
                        break
                myPop(left)
                if len(result) != 0:
                    left = result[len(result) - 1]
                else:
                    left = 9
                myAppend(nextR)
                right = nextR
                idx -= 1
                continue
        idx += 1
        for i in range(9, -1, -1):
            if visited[i] == 1:
                right = i
                myAppend(right)
                break
    return result


def inequality2(s):
    if s[0] == '<':
        myAppend(0)
        myAppend(1)
        left = 0
    else:
        myAppend(1)
        myAppend(0)
        left = 1
    myAppend(2)
    right = 2
    idx = 1
    while True:
        if idx == n:
            break
        if s[idx] == '>':
            if left > right:
                left = right
            else:
                myPop(right)
                for i in range(left + 1, n + 1):
                    if visited[i] == 1:
                        nextR = i
                        break
                myPop(left)
                if len(result) != 0:
                    left = result[len(result) - 1]
                else:
                    left = 0
                myAppend(nextR)
                right = nextR
                idx -= 1
                continue

        else:
            if left < right:
                left = right
            else:
                myPop(right)
                for i in range(0, right):
                    if visited[i] == 1:
                        myAppend(i)
                        right = i
                    break
                continue
        idx += 1
        for i in range(0, n + 1):
            if visited[i] == 1:
                right = i
                myAppend(right)
                break
    return result


def myPop(num):
    visited[num] = 1
    if len(result) > 0:
        del result[len(result) - 1]


def myAppend(num):
    visited[num] = 0
    result.append(num)


inputs = sys.stdin.readline
result = []
maxresult = []
minresult = []
n = int(inputs())
s = input().split()

visited = [1] * 10
maxresult = inequality(s)
print(''.join(list(map(str, maxresult))))
visited = [1] * 10
result = []
minresult = inequality2(s)
print(''.join(list(map(str, minresult))))
