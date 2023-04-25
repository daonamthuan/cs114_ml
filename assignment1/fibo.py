n = int(input())

def fibonacci (n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if n not in range (1, 31):
    print("So {} khong nam trong khoang [1, 30].".format(n))
else:
    print(fibonacci(n))

# for i in range (1, 31):
#     print(fibonacci(i))


