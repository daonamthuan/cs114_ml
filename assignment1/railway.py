k, t = input().split()
k, t = int(k), int(t)

count = t // k
if (count % 2 == 0):
    des = t % k;
else:
    des = k - t % k

print(des)