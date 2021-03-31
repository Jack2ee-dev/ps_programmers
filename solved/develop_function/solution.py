import math


def solution(progresses, speeds):
    answer = []

    days_to_complete = [math.ceil((100 - progresses[i]) / speeds[i])
                        for i in range(len(progresses))]

    while len(days_to_complete) > 0:
        completed_advance = days_to_complete.pop(0)
        completed = 1
        while len(days_to_complete) > 0 and completed_advance >= days_to_complete[0]:
            completed += 1
            days_to_complete.pop(0)
        answer.append(completed)

    return answer


if __name__ == "__main__":
    print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
