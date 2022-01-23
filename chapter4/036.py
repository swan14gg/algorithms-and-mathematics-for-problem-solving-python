from math import pi, cos

A, B, H, M = map(int, input().split())
Sr = 2 * pi * M / 60
Lr = 2 * pi * (60 * H + M) / 720
diff = max(Sr, Lr) - min(Sr, Lr)
diff = min(diff, 2 * pi - diff)
print((A ** 2 + B ** 2 - 2 * A * B * cos(diff)) ** 0.5)
