x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = map(int, input().split())
if x1 == x2 and x3 == x4:
    if x1 != x3:
        ans = "No"
    elif max(y1, y2) > max(y3, y4):
        if max(y3, y4) >= min(y1, y2):
            ans = "Yes"
        else:
            ans = "No"
    elif max(y3, y4) > max(y1, y2):
        if max(y1, y2) >= min(y3, y4):
            ans = "Yes"
        else:
            ans = "No"
    else:
        ans = "Yes"
elif x1 == x2 and x3 != x4:
    a34 = (y4 - y3) / (x4 - x3)
    b34 = y3 - a34 * x3
    y = a34 * x1 + b34
    if (
        min(x3, x4) <= x1 <= max(x3, x4)
        and min(y1, y2) <= y <= max(y1, y2)
        and min(y3, y4) <= y <= max(y3, y4)
    ):
        ans = "Yes"
    else:
        ans = "No"
elif x1 != x2 and x3 == x4:
    a12 = (y2 - y1) / (x2 - x1)
    b12 = y1 - a12 * x1
    y = a12 * x3 + b12
    if (
        min(x1, x2) <= x3 <= max(x1, x2)
        and min(y1, y2) <= y <= max(y1, y2)
        and min(y3, y4) <= y <= max(y3, y4)
    ):
        ans = "Yes"
    else:
        ans = "No"
else:
    a12 = (y2 - y1) / (x2 - x1)
    a34 = (y4 - y3) / (x4 - x3)
    b12 = y1 - a12 * x1
    b34 = y3 - a34 * x3
    if a12 == a34:
        if b12 != b34:
            ans = "No"
        else:
            if max(x1, x2) > max(x3, x4):
                if max(x3, x4) >= min(x1, x2):
                    ans = "Yes"
                else:
                    ans = "No"
            elif max(x3, x4) > max(x1, x2):
                if max(x1, x2) >= min(x3, x4):
                    ans = "Yes"
                else:
                    ans = "No"
            else:
                ans = "Yes"
    else:
        x = (b12 - b34) / (a34 - a12)
        if min(x1, x2) <= x <= max(x1, x2) and min(x3, x4) <= x <= max(x3, x4):
            ans = "Yes"
        else:
            ans = "No"

print(ans)
