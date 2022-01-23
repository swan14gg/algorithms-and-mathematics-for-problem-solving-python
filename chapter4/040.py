N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = []
for _ in range(M):
    B.append(int(input()))
C = [0]
for i in range(N - 1):
    C.append(C[i] + A[i])

ans = 0
for i, b in enumerate(B):
    if i == 0:
        now = b
        continue
    minB, maxB = min(now, b), max(now, b)
    ans += C[maxB - 1] - C[minB - 1]
    now = b

print(ans)
