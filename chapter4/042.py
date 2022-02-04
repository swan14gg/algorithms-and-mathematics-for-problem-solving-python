# O(N^1.5)となりTLE

N = int(input())

ans = 0
for i in range(1, N + 1):
    d = 0
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            d += 2
            if j ** 2 == i:
                d -= 1
    ans += d * i

print(ans)
