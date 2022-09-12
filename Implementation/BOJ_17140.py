#Date : 2022.09.12
#Update : 2022.09.12
#Classification : Implementation
#Author : leejian

import sys
input = sys.stdin.readline
def r_calculation():
    r = len(A)
    c = len(A[0])
    max_idx = 0
    for i in range(r):
        dict = {}
        sub_list = []
        for j in range(c):
            if A[i][j] == 0:
                continue
            if A[i][j] in dict:
                dict[A[i][j]] += 1
            else:
                dict[A[i][j]] = 1
        for key, item in dict.items():
            sub_list.append((key, item))
        sub_list.sort(key=lambda x: (x[1], x[0]))
        if len(sub_list) > 50:
            sub_list = sub_list[50:]
        A[i] = []
        for key, item in sub_list:
            A[i].extend([key, item])
        if max_idx < len(A[i]):
            max_idx = len(A[i])
    for i in range(r):
        if len(A[i]) < max_idx:
            A[i].extend([0]*(max_idx - len(A[i])))
def c_calculation():
    global A
    r = len(A)
    c = len(A[0])
    max_idx = 0
    total_list = []
    for i in range(c):
        dict = {}
        sub_list = []
        for j in range(r):
            if A[j][i] == 0:
                continue
            if A[j][i] in dict:
                dict[A[j][i]] += 1
            else:
                dict[A[j][i]] = 1
        for key, item in dict.items():
            sub_list.append((key, item))
        sub_list.sort(key=lambda x: (x[1], x[0]))
        if len(sub_list) > 50:
            sub_list = sub_list[50:]
        if max_idx < len(sub_list)*2:
            max_idx = len(sub_list)*2
        total_list.append(sub_list)
    A = [[0 for _ in range(c)] for _ in range(max_idx)]
    for i in range(c):
        for j in range(0, len(total_list[i])):
            A[j*2][i] = total_list[i][j][0]
            A[j*2+1][i] = total_list[i][j][1]

A = [[0 for _ in range(3)] for _ in range(3)]
R, C, K = map(int, input().split())
for i in range(3):
    A[i][0], A[i][1], A[i][2] = map(int, input().split())
time = 0
flag = False
for t in range(101):        #range(100) x -> range(101) o
    if R-1 < len(A) and C-1 < len(A[0]):
        if A[R-1][C-1] == K:
            flag = True
            print(t)
            break
    if len(A) >= len(A[0]):
        r_calculation()
    else:
        c_calculation()
if not flag:
    print(-1)
