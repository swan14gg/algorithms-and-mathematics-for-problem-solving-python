N = int(input())

A = [True] * (N + 1)

for i in range(2, int(N ** 0.5) + 1):
    if A[i]:
        x = 2 * i
        while x <= N:
            A[x] = False
            x += i

ans = []
for i, a in enumerate(A):
    if i < 2:
        continue
    if a:
        ans.append(i)

print(*ans)
