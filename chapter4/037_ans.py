Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())
Dx, Dy = map(int, input().split())

BAx = Ax - Bx
BAy = Ay - By
BCx = Cx - Bx
BCy = Cy - By
BDx = Dx - Bx
BDy = Dy - By
DCx = Cx - Dx
DCy = Cy - Dy
DAx = Ax - Dx
DAy = Ay - Dy
DBx = Bx - Dx
DBy = By - Dy

crossBAC = BAx * BCy - BCx * BAy
crossBAD = BAx * BDy - BDx * BAy
crossDCA = DCx * DAy - DAx * DCy
crossDCB = DCx * DBy - DBx * DCy

if crossBAC == crossBAD == crossDCA == crossDCB == 0:
    A = (Ax, Ay)
    B = (Bx, By)
    C = (Cx, Cy)
    D = (Dx, Dy)
    if A > B:
        tmp = B
        B = A
        A = tmp
    if C > D:
        tmp = D
        D = C
        C = tmp
    if max(A, C) <= min(B, D):
        print("Yes")
    else:
        print("No")
else:
    isAB = (crossBAC <= 0  and crossBAD >= 0) or (crossBAC >= 0  and crossBAD <= 0)
    isCD = (crossDCA <= 0  and crossDCB >= 0) or (crossDCA >= 0  and crossDCB <= 0)
    if isAB and isCD:
        print("Yes")
    else:
        print("No")
