# 17503_맥주 축제_실버1

import heapq

def drink():
    N, M, K = map(int, input().split())
    beers = [list(map(int, input().split())) for _ in range(K)]
    beers.sort(key=lambda x:(x[1], x[0]))

    pq = []
    preference = 0

    for beer in beers:
        preference += beer[0]
        heapq.heappush(pq, beer[0])

        if len(pq) == N:
            if preference >= M:
                return beer[1]
            else:
                preference -= heapq.heappop(pq)
    return -1

print(drink())