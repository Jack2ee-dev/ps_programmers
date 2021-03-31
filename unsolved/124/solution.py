def solution(n):
    answer = ''
    # 1 1, 2 2, 4 3, 11 4, 12 5, 14 6, 21 7, 22 8, 24 9, 41 10, 42 11, 44 12, 111, ...
    numbers = [4, 1, 2]

    while n > 0:
        answer = str(numbers[n % 3]) + answer
        if n // 3 == 1:
            break
        n = n // 3

    return answer


if __name__ == "__main__":
    print(solution(9))
