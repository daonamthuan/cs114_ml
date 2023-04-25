import sys

if __name__ == '__main__':
    my_set = set()
    while True:
        inp = sys.stdin.readline().strip()
        if inp == "0":
            break
        elif inp:
            a, b = map(int, inp.split())
            if a == 1:
                my_set.add(b)
            elif a == 3:
                my_set.discard(b)
            elif a == 2:
                if b in my_set:
                    print(1)
                else:
                    print(0)