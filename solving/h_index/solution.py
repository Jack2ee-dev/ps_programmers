def solution(citations):
    answer = 0
    citations.sort()
    l = len(citations)
    for i in range(l):
        c = citations[i]
        if c >= i:
            answer = min(answer, citations[i])
            print(answer)
    return answer


if __name__ == "__main__":
    print(solution([3, 0, 6, 1, 5]))