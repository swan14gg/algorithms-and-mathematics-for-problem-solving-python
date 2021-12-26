N, S = map(int, input().split())
A = list(map(int, input().split()))

ans = "No"
for i in range(2 ** N):
    sum_value = 0
    for j in range(N):
        if (i & (1 << j)) != 0:
            sum_value += A[j]
    if sum_value == S:
        ans = "Yes"
        break

print(ans)
