N, Q = map(int, input().split())
L = []
R = []
X = []
for _ in range(Q):
    l, r, x = map(int, input().split())
    L.append(l)
    R.append(r)
    X.append(x)
A = [0] * (N + 1)
for i in range(Q):
    A[L[i] - 1] += X[i]
    A[R[i]] -= X[i]

ans = ""
for i in range(1, N):
    if A[i] > 0:
        ans += "<"
    elif A[i] == 0:
        ans += "="
    else:
        ans += ">"

print(ans)
