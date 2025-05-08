# 10798_세로 읽기_브론즈 1

def main():
    arr = [input() for _ in range(5)]
    max_length = max(len(line) for line in arr)
    result = [arr[j][i] for i in range(max_length) for j in range(5) if i < len(arr[j])]
    print(''.join(result))

if __name__ == "__main__":
    main()