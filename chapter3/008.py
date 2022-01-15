N, S = map(int, input().split())
dp = [0] * (S + 1)
for i in range(S + 1):
    if i <= 1:
        continue
    tmp = 0
    for j in range(1, min(i // 2 + 1, N + 1)):
        if i - j <= N and i - j != j:
            tmp += 2
        elif i - j <= N and i - j == j:
            tmp += 1
    dp[i] = dp[i - 1] + tmp
print(dp[S])
