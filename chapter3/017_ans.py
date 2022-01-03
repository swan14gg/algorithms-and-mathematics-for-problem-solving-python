N = int(input())
A = list(map(int, input().split()))


def gcd(a: int, b: int) -> int:
    while a >= 1 and b >= 1:
        if a >= b:
            a = a % b
        else:
            b = b % a
    if a >= 1:
        return a
    return b


def lcm(a: int, b: int) -> int:
    return (a * b) // gcd(a, b)

ans = lcm(A[0], A[1])

for i in range(2, N):
    ans = lcm(ans, A[i])

print(ans)
