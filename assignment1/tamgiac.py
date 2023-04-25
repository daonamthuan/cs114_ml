import math

a = float(input())
b = float(input())
c = float(input())
p = (a + b + c) * 0.5
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
s = round(s, 2) if s - int(s) != 0 else int(s)


if a == b and b == c and c == a:
    print("Tam giac deu, dien tich = {}".format(s))
elif a == b or b == c or c == a:
    print("Tam giac can, dien tich = {}".format(s))
elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 +b**2 == a**2:
    print("Tam giac vuong, dien tich = {}".format(s))
elif a + b > c and c + a > b and b + c > a:
    print("Tam giac thuong, dien tich = {}".format(s))
else:
    print("Khong phai tam giac")