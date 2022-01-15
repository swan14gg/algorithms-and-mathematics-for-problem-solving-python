x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())
rb = max(r1, r2)
rs = min(r1, r2)
XYx = x1 - x2
XYy = y1 - y2
dist = (XYx ** 2 + XYy ** 2) ** 0.5 + rs

ans = 1
if dist == rb:
    ans = 2
elif dist > rb and dist < 2 * rs + rb:
    ans = 3
elif dist == 2 * rs + rb:
    ans = 4
elif dist > 2 * rs + rb:
    ans = 5
print(ans)
