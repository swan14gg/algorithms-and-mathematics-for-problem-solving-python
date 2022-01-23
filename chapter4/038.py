N, Q = map(int, input().split())
A = list(map(int, input().split()))
L = []
R = []
for _ in range(Q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
B = [0]
for i in range(N):
    B.append(B[i] + A[i])
for i in range(Q):
    print(B[R[i]] - B[L[i] - 1])
