import math

N = int(input())

ans = True
for i in range(2, int(math.sqrt(N)) + 1):
    if N % i == 0:
        ans = False
        break

print("YNeos"[not ans::2])
