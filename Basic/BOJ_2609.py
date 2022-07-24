#Date : 2022.07.23
#Update : 2022.07.23
#Classification : Brute-Force / recursion
#Author : https://velog.io/@junyp1/%EB%B0%B1%EC%A4%80-2609-Python-%EC%B5%9C%EB%8C%80%EA%B3%B5%EC%95%BD%EC%88%98%EC%99%80-%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98

import sys
input = sys.stdin.readline
n1, n2 = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
def lcm(a, b):
     return a*b//gcd(a, b)

print(gcd(n1, n2))
print(lcm(n1, n2))