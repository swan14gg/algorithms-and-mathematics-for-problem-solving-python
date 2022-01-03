N = int(input())
P = []
Q = []
for i in range(N):
    p, q = map(int, input().split())
    P.append(p)
    Q.append(q)
ans = 0
for i in range(N):
    ans += Q[i] / P[i]

print(ans)
