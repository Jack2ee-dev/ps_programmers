def solution(rows, columns, queries):
    answer = []
    matrix = []
    for i in range(rows):
        temp = []
        for j in range(1, columns + 1):
            temp.append(j)
        matrix.append(temp)

    for i in range(1, rows):
        for j in range(columns):
            matrix[i][j] += columns * i

    for q in queries:
        r1, c1, r2, c2 = q[0] - 1, q[1] - 1, q[2] - 1, q[3] - 1
        r1, r2 = min(r1, r2), max(r1, r2)
        c1, c2 = min(c1, c2), max(c1, c2)
        temp = []
        for i in range(c1, c2 + 1):
            temp.append(matrix[r1][i])
        for i in range(r1 + 1, r2 + 1):
            temp.append(matrix[i][c2])
        for i in range(c2 - 1, c1 - 1, -1):
            temp.append(matrix[r2][i])
        for i in range(r2 - 1, r1, -1):
            temp.append(matrix[i][c1])

        temp = [temp.pop()] + temp

        idx = 0
        for i in range(c1, c2 + 1):
            matrix[r1][i] = temp[idx]
            idx += 1
        for i in range(r1 + 1, r2 + 1):
            matrix[i][c2] = temp[idx]
            idx += 1
        for i in range(c2 - 1, c1 -1 , -1):
            matrix[r2][i] = temp[idx]
            idx += 1
        for i in range(r2 - 1, r1, -1):
            matrix[i][c1] = temp[idx]
            idx += 1
        answer.append(min(temp))

    return answer


if __name__ == "__main__":
    print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))