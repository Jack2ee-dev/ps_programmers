def solution(lottos, win_nums):
    lottos.sort()
    win_nums.sort()
    curr = 0
    i, j = 0, 0
    while True:
        if lottos[i] == win_nums[j]:
            curr += 1
            i += 1
            j += 1
        elif lottos[i] > win_nums[j]:
            j += 1
        else:
            i += 1
        if i >= len(lottos) or j >= len(win_nums):
            break

    min_correct = curr
    max_correct = curr
    for n in lottos:
        if n == 0:
            max_correct += 1

    min_rank = 7 - min_correct
    max_rank = 7 - max_correct
    if min_rank >= 6:
        min_rank = 6
    answer = [max_rank, min_rank]
    return answer


if __name__ == "__main__":
    print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
    print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
    print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))