N = int(input())
h = list(map(int, input().split()))

A = [0] * N

for i in range(N):
    if i == 0:
        continue
    if i == 1:
        A[i] = abs(h[i] - h[i - 1])
        continue
    A[i] = min(A[i - 1] + abs(h[i] - h[i - 1]), A[i - 2] + abs(h[i] - h[i - 2]))

print(A[N - 1])
