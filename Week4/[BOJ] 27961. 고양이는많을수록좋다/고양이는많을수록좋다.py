# 27961_고양이는 많을수록 좋다_브론즈1

def f():
    N = int(input())
    cnt, madoka_cat = 0, 0
    while madoka_cat < N:
        madoka_cat = min(N, max(madoka_cat + 1, madoka_cat * 2))
        cnt += 1
    return cnt

print(f())