# 2343_기타 레슨_실버1

def binary_search(videos, M):
    left, right = max(videos), sum(videos)
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        max_length, cnt = 0, 1
        cnt = 1

        for video in videos: # 최대 영상 길이에 따라 생성되는 블루레이 개수 구하기.
            if max_length + video > mid:
                cnt += 1
                max_length = 0
            max_length += video

        if cnt <= M:
            ans = mid
            right = mid - 1 # 더 작은 크기로
        else:
            left = mid + 1 # 더 큰 크기로

    return ans

def f():
    N, M = map(int, input().split())
    videos = list(map(int, input().split()))
    print(binary_search(videos, M))

f()