N = int(input())
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

ans = float("inf")
for i in range(N):
    for j in range(i + 1, N):
        XYx = X[j] - X[i]
        XYy = Y[j] - Y[i]
        ans = min(ans, (XYx ** 2 + XYy ** 2) ** 0.5)

print(ans)
