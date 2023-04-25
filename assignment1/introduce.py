n = int(input())
k = int(input())
p = int(input())
q = int(input())


def find(n, k, p, q):
    row, col = 0, 0
    if k % 2 == 0 and p - k/2 >= 0:
        row = p - k / 2
        col = q
    elif k % 2 == 0 and p - k/2 < 0:
        row = p + k / 2
        col = q
    elif k % 2 != 0:
        if q == 0 and p - k//2 - 1 >= 0:
            col = q + 1
            row = p - k // 2 - 1
        elif q == 0 and p - k//2 - 1 < 0:
            col = q + 1
            row = p + k // 2
        elif q == 1 and p - k//2 >= 0:
            col = q - 1
            row = p - k // 2
        elif q == 1 and p - k//2 < 0:
            col = q - 1
            row = p + k // 2 + 1
    row, col = int(row), int(col)
    if (n % 2 == 1 and row == n // 2 and col == 1) or row >= (n+1)//2:
        return -1
    else:
        return [row + 1, col + 1]

res = find(n, k, p - 1, q - 1)
if res != -1:
    print(res[0], res[1])
else:
    print(res)

