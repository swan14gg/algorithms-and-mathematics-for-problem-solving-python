N = int(input())
A = list(map(int, input().split()))
ans = A[0]
for a in A:
    while ans != 0 and a != 0:
        if ans >= a:
            ans = ans % a
        else:
            a = a % ans
    ans = max(ans, a)
print(ans)
