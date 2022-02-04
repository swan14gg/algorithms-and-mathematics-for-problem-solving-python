N = int(input())

A = [0] * (N + 1)

for i in range(1, N + 1):
    t = i
    while t <= N:
        A[t] += 1
        t += i

ans = 0
for i, a in enumerate(A):
    ans += i * a

print(ans)
