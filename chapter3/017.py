N = int(input())
A = list(map(int, input().split()))
ans_dict = {}
for a in A:
    tmp = {}
    for i in range(2, int(a ** 0.5) + 1):
        while a % i == 0:
            a //= i
            if i not in tmp:
                tmp[i] = 1
            else:
                tmp[i] += 1
    if a > 1:
        tmp[a] = 1
    for i in tmp.keys():
        if i not in ans_dict:
            ans_dict[i] = tmp[i]
        else:
            ans_dict[i] = max(ans_dict[i], tmp[i])

ans = 1
for i in ans_dict.keys():
    ans *= i ** ans_dict[i]
print(ans)
