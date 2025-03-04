# 11719_그대로 출력하기_브론즈3
import sys

def main():
    lines = sys.stdin.readlines()

    for line in lines:
        print(line, end='')

if __name__ == "__main__":
    main()