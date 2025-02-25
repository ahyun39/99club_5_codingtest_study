# 1697_숨바꼭질_실버1

from collections import deque

def bfs(N, K, times):
    q = deque()
    q.append((N, times))
    visited = [False] * 100001
    ans = float('inf')
    while q:
        x, time = q.popleft()
        visited[x] = True
        if x > 100000:
            break
        if x == K:
            if ans > time:
                ans = time
        if 0 <= x - 1 < 100001 and not visited[x-1]:
            q.append((x - 1, time + 1))
        if x + 1 < 100001 and not visited[x+1]:
            q.append((x + 1, time + 1))
        if 2 * x < 100001 and not visited[2*x]:
            q.append((2 * x, time + 1))

    return ans


def f():
    N, K = map(int, input().split())
    if N == K: print(0) # 수빈과 동생의 현재 위치가 동일한 경우
    else: print(bfs(N, K, 0))

f()