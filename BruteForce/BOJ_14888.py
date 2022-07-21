#Date : 2022.07.21
#Update : 2022.07.21
#Classification : Brute-Force / recursion
#Author : leejian


import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
op_list = list(map(int, input().split()))

def calcul(idx, res, operand):
    global min, max
    if idx == n:
        if res < min:
            min = res
        if res > max:
            max = res
        return
    for i in range(len(operand)):
        if operand[i] > 0:
            result = arith(res, num[idx], i)
            operand[i] = operand[i] - 1
            calcul(idx+1, result, operand)
            operand[i] = operand[i] + 1

def arith(num1, num2, op):
    if op == 0:
        return num1 + num2
    elif op == 1:
        return num1 - num2
    elif op == 2:
        return num1 * num2
    else:
        return int(num1 / num2)   # num1//num2 랑 다름을 주의

min = 1000000000
max = -1000000000
calcul(1, num[0], op_list)

print(max)
print(min)