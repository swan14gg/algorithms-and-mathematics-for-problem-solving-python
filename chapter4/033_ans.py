ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

BAx = ax - bx
BAy = ay - by
BCx = cx - bx
BCy = cy - by
CAx = ax - cx
CAy = ay - cy
CBx = bx - cx
CBy = by - cy

if BAx * BCx + BAy * BCy < 0:
    ans = (BAx ** 2 + BAy ** 2) ** 0.5
elif CAx * CBx + CAy * CBy < 0:
    ans = (CAx ** 2 + CAy ** 2) ** 0.5
else:
    ans = abs((BAx * BCy) - (BAy * BCx)) / (BCx ** 2 + BCy ** 2) ** 0.5

print(ans)
