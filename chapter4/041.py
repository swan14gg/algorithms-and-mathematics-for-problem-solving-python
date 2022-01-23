T = int(input())
N = int(input())
L = []
R = []
for _ in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
A = [0] * T
for i in range(N):
    A[L[i]] += 1
    if R[i] < T:
        A[R[i]] -= 1
for i in range(T):
    if i == 0:
        now = A[i]
        print(now)
        continue
    now += A[i]
    print(now)
