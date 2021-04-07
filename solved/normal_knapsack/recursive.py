N, K = map(int, input().split())
W, V = [0] * (N + 1), [0] * (N + 1)
for i in range(1, N + 1):
    W[i], V[i] = map(int, input().split())
dp = [dict() for _ in range(N + 1)]


def knapsack(i, w):
    if w in dp[i]:
        return dp[i][w]

    if i <= 0 or w <= 0:
        return 0

    if W[i] <= w:
        value = max(knapsack(i - 1, w), knapsack(i - 1, w - W[i]) + V[i])
    else:
        value = knapsack(i - 1, w)

    dp[i][w] = value
    return value


print(knapsack(N, K))
