def solution(n):
    dp = [0] * 100001
    dp[0] = 1
    dp[1] = 1
    dp[2] = 3
    dp[3] = 10
    rep_cnt = [0, 1, 2, 6, 1]
    initial_cnt = [0, 1, 2, 5, 2, 2, 4]
    # 점하식으로 계산하기 전에 초기 값을 세팅 (4 ~ 6)
    for j in range(4, 7):
        for k in range(1, j + 1):
            dp[j] += dp[j - k] * initial_cnt[k]
    # 7 ~
    for i in range(7, n + 1):
        cnt = 0
        for j in range(1, 5):
            cnt += dp[i - j] * rep_cnt[j]
        cnt -= dp[i - 6]
        dp[i] = cnt
    return dp[n] % 1000000007