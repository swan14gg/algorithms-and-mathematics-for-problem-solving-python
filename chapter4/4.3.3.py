l = 1
r = 2

for _ in range(1, 100 + 1):
    m = (r + l) / 2
    print(m)
    if m ** 2 < 2:
        l = m
    else:
        r = m
