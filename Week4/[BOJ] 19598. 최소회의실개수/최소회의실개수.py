# 19598_최소 회의실 개수_골드5

import heapq

def meeting_room():
    N = int(input())
    meetings = [list(map(int, input().split())) for _ in range(N)]
    meetings.sort()  # 회의 시작 시간을 기준으로 정렬
    pq = []  # 우선순위 큐 생성
    heapq.heappush(pq, meetings[0][1])  # 1번째 회의 종료 시간을 힙에 push
    
    for i in range(1, N):
        start, end = meetings[i]
        if pq[0] <= start:  # 기존 회의가 끝났으면 pop
            heapq.heappop(pq)
        heapq.heappush(pq, end)  # 현재 회의를 새로운 회의실에 배정
    return len(pq)  # pq에 남아있는 원소의 개수가 필요한 회의실 개수

print(meeting_room())