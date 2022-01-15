ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

if (ax - bx) * (cx - bx) + (ay - by) * (cy - by) < 0 or (ax - cx) * (bx - cx) + (ay - cy) * (by - cy) < 0:
    ans = min(
        ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5,
        ((ax - cx) ** 2 + (ay - cy) ** 2) ** 0.5,
    )
else:
    A = (by - cy) / (bx - cx)
    B = by - A * bx
    A_ = -1 / A
    B_ = ay - A_ * ax
    x = (B - B_) / (A_ - A)
    y = A * x + B
    ans = ((ax - x) ** 2 + (ay - y) ** 2) ** 0.5

print(ans)
