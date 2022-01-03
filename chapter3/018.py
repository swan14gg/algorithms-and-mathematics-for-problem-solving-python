# 全探索でO(N^2)となりTLE

N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(N):
    target = 500 - A[i]
    ans += A[i + 1 :].count(target)

print(ans)
