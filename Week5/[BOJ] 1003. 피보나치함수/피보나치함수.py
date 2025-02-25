# 1003_피보나치 함수_실버3

def main():
    T = int(input())
    dp = [(1, 0), (0, 1)] + [(0, 0)] * 39  # N은 최대 40을 갖음 # dp 초기화
    
    # fibo(n-1) + fibo(n-2) 로 0, 1 반환 count 구하는 코드로 구현
    for i in range(2, 41):
        dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])
    
    for _ in range(T):
        N = int(input())
        print(dp[N][0], dp[N][1]) # 0이 출력되는 횟수, 1이 출력되는 횟수

if __name__ == "__main__":
    main()