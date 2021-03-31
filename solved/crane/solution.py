def solution(board, moves):
    answer = 0

    moves = list(map(lambda move: move - 1, moves))
    stack = []

    for move in moves:
        for row in board:
            pick = row[move]
            if row[move] == 0:
                continue
            else:
                if len(stack) == 0 or stack[-1] != pick:
                    stack.append(row[move])
                    row[move] = 0
                    break
                elif len(stack) > 0 and stack[-1] == pick:
                    stack.pop()
                    row[move] = 0
                    answer += 2
                    break

    return answer


if __name__ == "__main__":
    print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [
          4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]	))
