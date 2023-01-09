# Date : 2023.01.08
# Update : 2023.01.08
# Classification : Brute-Force / permutation
# Author : leejian
# 1차 알고리즘 - 시간초과

import sys


def check(left, right, op):
    if op == '>' and left < right:
        return False
    elif op == '<' and left > right:
        return False
    else:
        return True

def dfs2(depth):
    global result, maxRes
    if depth == alphaNum:       # 순열의 경우의 수 중 하나가 완성
        inequality(combi)       # 알파벳에 순열의 숫자대로 배정
        result = 0
        for word in s:          # 알파벳으로 이루어진 문자열을 숫자로 변환
            num = 0
            for i in range(len(word)):
                num *= 10
                num += dict[word[i]]
            result += num
        if result > maxRes:     # 완성된 결과값이 현 최댓값보다 크면 갱신
            maxRes = result
    for idx in range(0, alphaNum):
        if visited[idx] == 0:
            combi[depth] = number[idx]
            visited[idx] = 1
            dfs2(depth + 1)
            visited[idx] = 0


def inequality(data):
    for i in range(len(keys)):
        dict[keys[i]] = data[i]

inputs = sys.stdin.readline

flag = True
n = int(inputs())
s = []
dict = {}
for i in range(n):
    s.append(inputs().strip())
    for j in range(len(s[i])):
        if not dict.get(s[i][j]):
            dict[s[i][j]] = -1

alphaNum = len(dict)
visited = [0] * 10
number = [i for i in range(9, 9-alphaNum, -1)]
keys = list(dict.keys())
combi = [0] * 10
result = 0
maxRes = 0
dfs2(0)
print(maxRes)



import sys


def check(left, right, op):
    if op == '>' and left < right:
        return False
    elif op == '<' and left > right:
        return False
    else:
        return True

def dfs2(depth):
    global flag
    if depth == n+1:
        if inequality(combi):
            flag = False
            return
    for idx in range(0, n+1):
        if flag:
            if visited[idx] == 0:
                combi[depth] = number[idx]
                visited[idx] = 1
                dfs2(depth + 1)
                visited[idx] = 0
        else:
            break

def inequality(data):
    for i in range(0, n):
        if s[i] == '>' and data[i] < data[i+1]:
            return False
        elif s[i] == '<' and data[i] > data[i+1]:
            return False
        else:
            continue
    return True

inputs = sys.stdin.readline
n = int(inputs())
s = input().split()

# 최댓값 구하기
flag = True
visited = [0] * 10
number = [i for i in range(9, 8-n, -1)]
combi = [0] * (n+1)
dfs2(0)
print(''.join(list(map(str, combi))))

# 최솟값 구하기
flag = True
visited = [0] * (n+1)
number = [i for i in range(0, n+1)]
dfs2(0)
print(''.join(list(map(str, combi))))



# 풀이 방법 요약
## 기본 원리
배치해야할 숫자가 n개일때 최댓값은 9부터 1씩 작아지며 숫자 n개를 선택, 최솟값은 0부터 커지며 숫자 n개를 선택해서 배열해야 함
    ex) n = 3 일때 최댓값에 포함되는 숫자는 9, 8, 7 이고 최솟값에 포함되는 숫자는 0, 1, 2 임
1. 최댓값 또는 최솟값에 포함되는 숫자를 선정
2. 해당 숫자들의 순열들을 하나씩 검사해서 모든 부등호 크기 비교에 성립하는지 검사
    이때, 최댓값은 순열 검사 순서를 큰 것에서부터 작은 순서로 하고 최솟값은 작은 것부터 큰 것으로 함
3. 따라서, 처음으로 부등호 크기 비교를 모두 만족하는 숫자가 최댓값 혹은 최솟값이 됨

# 느낀점
처음에 알고리즘을 세부적으로 짜서 알고리즘 끝에 한 번에 답을 내도록 했었는데
그것보다 가능한 경우의 수를 구해서 그게 성립하는지 검사하는 방식이 더 나을 때도 있다는 것을 느낌

대소비교에 관한 문제는 숫자 자체의 값보다 '그 자리에 전체에서 몇 번째로 큰 숫자가 와야하는지' 가
더 중요하다는 생각이 들었음
