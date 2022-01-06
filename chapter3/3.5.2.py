import random

count = [0] * 10
for i in range(len(count)):
    for _ in range(1000000):
        x = random.random() * 6
        y = random.random() * 9
        count[i] += ((x - 3) ** 2 + (y - 3) ** 2) ** 0.5 <= 3 or (
            (x - 3) ** 2 + (y - 7) ** 2
        ) ** 0.5 <= 2

print(54 * (sum(count) / 10) / 1000000)
