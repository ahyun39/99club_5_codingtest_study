# 1051_숫자 정사각형_실버3

def check_square(board, size):
    for i in range(N-size+1):
        for j in range(M-size+1):
            if board[i][j] == board[i+size-1][j] == board[i][j+size-1] == board[i+size-1][j+size-1]:
                return True
    return False

def f():
    global N, M
    N, M = map(int, input().split())
    board = [str(input()) for _ in range(N)]
    size = min(N, M)
    max_square = 0

    for s in range(1, size+1):
        if check_square(board, s):
            max_square = max(max_square, s*s)
    return max_square

print(f())