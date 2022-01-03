N = int(input())
A = list(map(int, input().split()))
M = [0] * 100000
for a in A:
    M[a] += 1
ans = 0
for i in range(1, 50000):
    ans += M[i] * M[100000 - i]
ans += (M[50000] * (M[50000] - 1)) // 2
print(ans)
