from collections import deque
import sys

if __name__ == '__main__':
    d = deque()
    my_dict = dict()

    while True:
        inp = sys.stdin.readline().strip()
        if inp == "6":
            break

        elif inp[0] == "0":
            k, n = map(int, inp.split())
            d.appendleft(n)
            if n in my_dict.keys():
                #my_dict[n] += 1
                pass
            else:
                my_dict.update({n: 1})

        elif inp[0] == "1":
            k, n = map(int, inp.split())
            d.append(n)
            if n in my_dict.keys():
                # my_dict[n] += 1
                pass
            else:
                my_dict.update({n: 1})

        elif inp[0] == "2":
            k, a, b = map(int, inp.split())
            if a in my_dict.keys():
                d.insert(d.index(a) + 1, b)
            else:
                d.appendleft(b)
            if b in my_dict.keys():
                # my_dict[b] += 1
                pass
            else:
                my_dict.update({b: 1})
        elif inp[0] == "3":
            k, n = map(int, inp.split())
            if n in my_dict.keys():
                d.remove(n)
                if my_dict[n] == 1:
                    # my_dict.pop(n)
                    pass
                else:
                    # my_dict[n] -= 1
                    pass

        elif inp[0] == "4":
            k, n = map(int, inp.split())
            if n in my_dict.keys():
                d = deque(x for x in d if x != n)
                if my_dict[n] == 1:
                    my_dict.pop(n)
                else:
                    my_dict[n] -= 1

        elif inp == "5":
            if d:
                n = d.popleft()
                if my_dict[n] == 1:
                    my_dict.pop(n)
                else:
                    my_dict[n] -= 1

    for x in d:
        print(x, end=" ")
    print(my_dict)