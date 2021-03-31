def solution(skill, skill_trees):
    answer = 0
    skill_list = list(skill)

    for skill_tree in skill_trees:
        skill_tree_list = list(skill_tree)
        skill_tree_idx = []
        for skill in skill_tree_list:
            if skill in skill_list:
                skill_tree_idx.append(skill_list.index(skill))
        if len(skill_tree_idx) == 0:
            answer += 1
        elif len(skill_tree_idx) == 1 and skill_tree_idx[0] == 0:
            answer += 1
        else:
            if diff_one(skill_tree_idx) == True:
                answer += 1

    return answer


def diff_one(skill_tree_idx):
    if len(skill_tree_idx) >= 1:
        if skill_tree_idx[0] != 0:
            return False

    for i in range(1, len(skill_tree_idx)):
        if (skill_tree_idx[i] - skill_tree_idx[i-1] != 1):
            return False
    return True


if __name__ == "__main__":
    print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
