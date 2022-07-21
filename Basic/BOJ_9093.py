import sys

n = int(sys.stdin.readline())
for i in range(n):
    word_list = sys.stdin.readline().strip().split()
    s = ""
    for word in word_list:
        l = list(word)
        for j in range(len(l)//2):
            temp = l[j]
            l[j] = l[len(word)-1-j]
            l[len(l)-1-j] = temp
        s = s + "".join(l) + " "
    print(s)