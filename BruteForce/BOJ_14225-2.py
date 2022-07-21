#Date : 2022.07.21
#Update : 2022.07.21
#Classification : Brute-Force / recursion
#Author : https://zoeful-log.tistory.com/84 [Zoe_ful:티스토리]

input()
a=0
for i in [*sorted(map(int,input().split()))]:
    if a+1<i:break
    a+=i
print(a+1)