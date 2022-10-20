def insertionSort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
    while j >= 0 and a[j][0] >= key[0]: # 등호 추가시 stable 보장 안 됨
        a[j+1] = a[j]
        j = j-1
    a[j+1] = key

a = [(1, 3), (2, 1), (2, 2), (2, 3), (1, 4)]
insertionSort(a)
print(a)
# [(1, 4), (1, 3), (2, 1), (2, 2), (2, 3)]
