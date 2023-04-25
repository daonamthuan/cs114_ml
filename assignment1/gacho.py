con, chan = input().split()
con, chan = int(con), int(chan)

for i in range(1, chan//4+1):
    if 4 * i + (con - i) * 2 == chan:
        print(con-i, i)