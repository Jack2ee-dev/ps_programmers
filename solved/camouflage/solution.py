def solution(clothes):
    c_dict = dict()
    for c in clothes:
        if c[1] not in c_dict:
            c_dict[c[1]] = [c[0]]
        else:
            c_dict[c[1]].append(c[1])

    answer = 1
    for key in c_dict.keys():
        answer *= len(c_dict[key]) + 1

    answer -= 1

    return answer


if __name__ == "__main__":
    print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
