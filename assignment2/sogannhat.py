n = int(input())
a = [int(x) for x in input().split()]
k, x = input().split()
k, x = int(k), int(x)


# find the nearest number
def find(a, n, x):
    temp, idx = abs(a[0] - x), 0
    for i in range(1, n):
        if abs(a[i] - x) < temp:
            temp = abs(a[i] - x)
            idx = i
    return idx


idx = find(a, n, x)
i, j = idx - 1, idx + 1

count = 1
res = [a[idx]]


while count < k:
    if i < 0:
        res.append(a[j])
        j += 1
        count += 1
    elif j >= n:
        res.append(a[i])
        i -= 1
        count += 1
    elif abs(a[i] - x) < abs(a[j] - x):
        res.append(a[i])
        i -= 1
        count += 1
    elif abs(a[i] - x) > abs(a[j] - x):
        res.append(a[j])
        j += 1
        count += 1
    else:
        res.append(a[i])
        i -= 1
        count += 1

res.sort()
#" ".join(str(x) for x in res)
print(" ".join(str(x) for x in res))