class Request:
    def __init__(self, priority):
        self.priority = priority


def solution(priorities, location):
    p_list = []
    for priority in priorities:
        p_list.append(Request(int(priority)))

    p_focus = p_list[location]
    answer = 1
    while p_list:
        p_curr = p_list.pop(0)
        out = True
        for i in range(0, len(p_list)):
            if p_curr.priority < p_list[i].priority:
                p_list.append(p_curr)
                out = False
                break
        if (p_curr is p_focus) and (out is True):
            break
        elif out is True:
            answer += 1

    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
