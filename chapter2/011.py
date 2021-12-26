import math

N = int(input())
A = []
for i in range(2, N + 1):
    if i == 2:
        A.append(str(i))
        continue
    if i % 2 == 0:
        continue
    for j in range(3, int(math.sqrt(i)) + 1, 2):
        if i % j == 0:
            break
    else:
        A.append(str(i))

print(" ".join(A))
