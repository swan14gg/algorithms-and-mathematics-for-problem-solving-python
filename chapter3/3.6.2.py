A = [4, 1, 6, 3, 2, 6, 9, 8, 5, 2]
N = len(A)


def swap(a, b):
    tmp = A[a]
    A[a] = A[b]
    A[b] = tmp


for i in range(N):
    for j in range(N):
        if A[i] < A[j]:
            swap(i, j)

print(A)
