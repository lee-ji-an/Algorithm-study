import sys


def solve(s, N):
    bit = 0
    ans = -1
    string = ""
    ans_bit = (1 << (N + 1)) - 2
    for i in range(len(s)):
        num = int(s[i])
        if not (1 <= num <= N):
            string = ""
            bit = 0
            continue
        if bit & (1 << num) == 1:
            string = s[i]
            bit = (1 << num)

        else:  # 0
            bit = bit | (1 << num)
            string = string + s[i]

        if bit == ans_bit:
            ans = max(int(string), ans)
            string = ""
            bit = 0

    return ans
def solution(s, N):
    ans = -1
    for i in range(len(s) - N + 1):
        bit = 0
        string = ""
        num_set = set([n for n in range(1, N + 1)])
        for j in range(i, i + N):
            if int(s[j]) in num_set:
                num_set.remove(int(s[j]))
                string = string + s[j]
            else:
                string = "-1"
                break
        print(string)
        ans = max(ans, int(string))
    return ans

print(solve("31325", 2))
print(solve("121", 2))
print(solution("121", 2))
