N = int(input())
A = list(map(int, input().split()))

a, b, c, d = 0, 0, 0, 0
for i in range(N):
    if A[i] == 100:
        a += 1
    elif A[i] == 200:
        b += 1
    elif A[i] == 300:
        c += 1
    else:
        d += 1

print(a * d + b * c)
