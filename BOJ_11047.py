import sys
price_list = []
total_price = 0
min_idx = 0
cnt = 0
n, k = input().split()
n = int(n)
k = int(k)

for i in range(n):
    price_list.append(int(sys.stdin.readline()))

for i in range(n-1, -1, -1):
    if k == 0: break
    if price_list[i]>k: continue
    cnt = cnt + k//price_list[i]
    k = k % price_list[i]

print(cnt)