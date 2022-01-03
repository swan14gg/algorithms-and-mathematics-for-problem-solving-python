N = int(input())
A = list(map(int, input().split()))

a = b = c = 0
for i in range(N):
    if A[i] == 1:
        a += 1
    elif A[i] == 2:
        b += 1
    else:
        c += 1


def calc(n):
    return (n * (n - 1)) // 2


print(calc(a) + calc(b) + calc(c))
