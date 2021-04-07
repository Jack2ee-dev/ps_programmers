def solution(N, number):
    dp = [{0}, {N}]

    for idx in range(1, 9):
        if number in dp[idx]:
            return idx
        new = {N * int("1" * (idx + 1))}
        for e1 in dp[idx]:
            for e2 in dp[-idx]:
                new.add(e1 + e2)
                new.add(e1 - e2)
                new.add(e2 - e1)
                new.add(e1 * e2)
                if e2 != 0:
                    new.add(e1 // e2)
                if e1 != 0:
                    new.add(e2 // e1)
        dp.append(new)
        idx += 1

    return idx


if __name__ == "__main__":
    print(solution(2, 11))
