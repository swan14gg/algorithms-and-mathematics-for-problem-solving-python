N = int(input())
A = [0] * (N + 1)
for i in range(N + 1):
    if i in [0, 1]:
        A[i] = 1
        continue
    A[i] = A[i - 1] + A[i - 2]
print(A[N])
