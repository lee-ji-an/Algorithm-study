#Date : 2022.07.23
#Update : 2022.07.23
#Classification : Brute-Force / recursion
#Author : leejian

import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
op_list = list(map(int, input().split()))

def calcul(idx, res):
    global min, max
    if idx == n:
        if res < min:
            min = res
        if res > max:
            max = res
        return
    else:
        if op_list[0] > 0:
            op_list[0] = op_list[0] - 1
            calcul(idx + 1, res + num[idx])
            op_list[0] = op_list[0] + 1

        if op_list[1] > 0:
            op_list[1] = op_list[1] - 1
            calcul(idx + 1, res - num[idx])
            op_list[1] = op_list[1] + 1

        if op_list[2] > 0:
            op_list[2] = op_list[2] - 1
            calcul(idx + 1, res * num[idx])
            op_list[2] = op_list[2] + 1

        if op_list[3] > 0:
            op_list[3] = op_list[3] - 1
            calcul(idx + 1, int(res / num[idx]))
            op_list[3] = op_list[3] + 1

min = 1000000000
max = -1000000000

calcul(1, num[0])
print(max)
print(min)
