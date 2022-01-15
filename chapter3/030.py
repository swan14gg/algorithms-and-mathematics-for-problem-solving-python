N, W = map(int, input().split())
w = []
v = []
for i in range(N):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)
dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
for i in range(N + 1):
    for j in range(W + 1):
        if i == 0:
            break
        if j - w[i - 1] >= 0:
            dp[i][j] = max(dp[i - 1][j - w[i - 1]] + v[i - 1], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][W])
