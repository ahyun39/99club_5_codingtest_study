# 2225_합분해_골드5

def f():
    N, K = map(int, input().split())
    dp = [[0] * (N + 1) for _ in range(K + 1)]
    dp[0][0] = 1

    # DP 계산
    for k in range(1, K + 1):
        dp[k][0] = 1
        for n in range(1, N + 1):
            dp[k][n] = (dp[k][n-1] + dp[k-1][n]) % 1000000000

    print(dp[K][N])

f()