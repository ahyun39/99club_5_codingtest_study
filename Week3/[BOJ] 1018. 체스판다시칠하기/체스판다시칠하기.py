# 1018_체스판 다시 칠하기_실버4

def check_pattern(board):
    pattern1 = ['WBWBWBWB', 'BWBWBWBW'] * 4  # 시작이 W인 패턴
    pattern2 = ['BWBWBWBW', 'WBWBWBWB'] * 4  # 시작이 B인 패턴

    replace1 = sum(board[i][j] != pattern1[i][j] for i in range(8) for j in range(8))
    replace2 = sum(board[i][j] != pattern2[i][j] for i in range(8) for j in range(8))

    return min(replace1, replace2)

def f():
    N, M = map(int, input().split())
    board = [input().strip() for _ in range(N)]

    min_ans = float('inf')

    for i in range(N - 7):
        for j in range(M - 7):
            compare_board = [board[x][j:j+8] for x in range(i, i+8)]
            min_ans = min(min_ans, check_pattern(compare_board))

    return min_ans

print(f())