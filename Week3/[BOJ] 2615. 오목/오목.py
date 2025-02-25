# 2615_오목_실버1

def check(board, i, j, d1, d2):
    cnt, ax, ay = 1, i, j

    for dx, dy in [(d1, d2), (-d1, -d2)]:
        nx, ny = i + dx, j + dy
        while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == board[i][j]:
            cnt += 1
            if dx == d1 and dy == d2:
                ax, ay = nx, ny
            nx, ny = nx + dx, ny + dy

    return (cnt == 5, ax, ay) if cnt == 5 else (False, -1, -1)

def f():
    board = [list(map(int, input().split())) for _ in range(19)]
    directions = [(-1, -1), (1, 1), (1, -1), (-1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(19):
        for j in range(19):
            if board[i][j] in [1, 2]:
                for k in range(0, 8, 2):
                    is_valid, x, y = check(board, i, j, *directions[k])
                    if is_valid:
                        print(board[i][j])
                        print(x + 1, y + 1)
                        return
    print(0)

f()