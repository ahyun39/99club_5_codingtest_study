# 11053_가장 긴 증가하는 부분 수열_실버2

from bisect import bisect_left

def lis_optimized(l, A):
    sub = []  # LIS를 유지하는 배열

    for num in A:
        idx = bisect_left(sub, num)  # num이 들어갈 위치 탐색

        if idx == len(sub):
            sub.append(num)  # num이 LIS의 가장 큰 값이면 추가
        else:
            sub[idx] = num  # LIS 내 적절한 위치의 값을 num으로 대체

    return len(sub)  # LIS의 길이 반환

def main():
    l = int(input())
    A = list(map(int, input().split()))
    print(lis_optimized(l, A))

if __name__ == "__main__":
    main()