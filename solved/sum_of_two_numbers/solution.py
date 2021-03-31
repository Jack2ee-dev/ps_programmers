def solution(numbers):
    _set = set()

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                _set.add(numbers[i] + numbers[j])

    l = list(_set)
    l.sort()

    return l


if __name__ == "__main__":
    print(solution([2, 1, 3, 4, 1]))
