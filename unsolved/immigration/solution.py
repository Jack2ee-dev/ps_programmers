def solution(n, times):
    answer = float('inf')
    left = min(times)
    right = max(times) * n

    while left <= right:
        mid = (left + right) // 2

        possible = 0
        for time in times:
            possible += mid // time

        if possible < n:
            left = mid + 1
        else:
            answer = min([answer, mid])
            right = mid - 1

    return answer


if __name__ == "__main__":
    print(solution(6, [7, 10]))
