def solution(e, starts):
    dp = [0] * (e + 1)
    dp[1] = 1
    for i in range(2, e + 1):
        for j in range(i, e + 1, i):
            dp[j] += 2
    for i in range(2, int(e ** (0.5)) + 1):
        dp[i * i] -= 1

    dp_ans = [0] * (e + 1)
    max_value = 0
    for i in range(e, 0, -1):
        if max_value <= dp[i]:
            max_value = dp[i]
            dp_ans[i] = i
        else:
            dp_ans[i] = dp_ans[i + 1]

    answer = [0] * len(starts)
    for i in range(len(starts)):
        answer[i] = dp_ans[starts[i]]

    return answer