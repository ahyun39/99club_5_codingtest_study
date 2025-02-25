# 15686_치킨 배달_골드5

from itertools import combinations

def chicken():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    chickens = [(i, j) for i in range(N) for j in range(N) if board[i][j] == 2]
    houses = [(i, j) for i in range(N) for j in range(N) if board[i][j] == 1]

    min_dist = float('inf')

    for selected in combinations(chickens, M):
        total_dist = 0
        for hx, hy in houses:
            house_to_chicken = float('inf')
            for cx, cy in selected:
                house_to_chicken = min(house_to_chicken, abs(hx - cx) + abs(hy - cy))
            total_dist += house_to_chicken
        min_dist = min(min_dist, total_dist)

    print(min_dist)

chicken()