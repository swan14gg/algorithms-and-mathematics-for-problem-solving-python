r = 1000
a = 2

for i in range(1, 10 + 1):
    print(a)
    zahyou_x = a
    zahyou_y = a * a * a * a * a * a * a * a * a * a
    sessen_a = (
        10
        * zahyou_x
        * zahyou_x
        * zahyou_x
        * zahyou_x
        * zahyou_x
        * zahyou_x
        * zahyou_x
        * zahyou_x
        * zahyou_x
    )
    sessen_b = zahyou_y - sessen_a * zahyou_x
    a = (r - sessen_b) / sessen_a
