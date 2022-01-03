n, r = map(int, input().split())

def calc(a):
    val = 1
    for i in range(1, a + 1):
        val *= i
    return val

print(calc(n) // (calc(r) * calc(n - r)))
