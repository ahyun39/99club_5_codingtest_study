# 1351_무한 수열_골드5

def f():
    N, P, Q = map(int, input().split())
    dp = {0:1}  # 딕셔너리 기반 메모이제이션  # dp[0] = 1

    def memo(n):
        if n in dp:  # 이미 계산된 값이면 그대로 반환
            return dp[n]
        dp[n] = memo(n // P) + memo(n // Q)
        return dp[n]

    print(memo(N))

f()