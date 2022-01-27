r = 2
a = 2

for i in range(1, 10 + 1):
    print(a)
    zahyou_x = a
    zahyou_y = a * a * a
    sessen_a = 3 * (zahyou_x ** 2)
    sessen_b = zahyou_y - sessen_a * zahyou_x
    a = (r - sessen_b) / sessen_a
