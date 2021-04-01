# [출처](https://programmers.co.kr/learn/courses/30/lessons/12982)

def solution(d, budget):
    answer = 0
    d.sort()
    b_sum = 0

    for each in d:
        if b_sum > budget:
            break
        b_sum += each
        if b_sum > budget:
            break
        answer += 1

    return answer


print(solution([1, 3, 2, 5, 4], 9))
