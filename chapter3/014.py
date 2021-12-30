import math

N = int(input())
ans = []
ok = False
while not ok:
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            ans.append(str(i))
            N //= i
            break
    else:
        ans.append(str(N))
        ok = True

print(" ".join(ans))
