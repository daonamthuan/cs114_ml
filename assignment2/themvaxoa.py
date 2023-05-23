# from collections import deque
#
# # def insert_after(a, b, d):
# #     if a in d:
# #         index = d.index(a)
# #         d.insert(index + 1, b)
# #     else:
# #         d.appendleft(b)
# #
# # def remove(n, d):
# #     if n in d:
# #         d.remove(n)
# #
# # def remove_all(n, d):
# #     for x in list(d):
# #         if x == n:
# #             d.remove(x)
# #
# #
# # if __name__ == '__main__':
# #     d = deque()
# #     while True:
# #         inp = input().strip()
# #         if inp == "6":
# #             break
# #         k, *arg = map(int, inp.split())
# #
# #         if k == 5:
# #             try:
# #                 d.popleft()
# #             except:
# #                 continue
# #         elif k == 0:
# #             d.appendleft(*arg)
# #         elif k == 1:
# #             d.append(*arg)
# #         elif k == 2:
# #             insert_after(*arg, d)
# #         elif k == 3:
# #             remove(*arg, d)
# #         elif k == 4:
# #             remove_all(*arg, d)
# #     print(" ".join(str(x) for x in d) if len(d) > 0 else "blank")
#
#
#
# def remove_all(n, d):
#     while n in d:
#         d.remove(n)
# import sys
# from collections import deque
#
#
# def add_left(n, d):
#     d.appendleft(n)
#
#
# def add_right(n, d):
#     d.append(n)
#
#
# def remove(n, d):
#     if n in d:
#         d.remove(n)
#
# #
# # def remove_all(n, d):
# #     for x in list(d):
# #         if x == n:
# #             d.remove(x)
#
# # def remove_all(n, d):
# #     d = deque([x for x in d if x != n])
# #     # return d
#
#
# def remove_all(n, p):
#     global d
#     d = deque(x for x in d if x != n)
#     # return d
#
#
# def insert_after(a, b, d):
#     try:
#         index = d.index(a)
#         d.insert(index + 1, b)
#     except:
#         d.appendleft(b)
#
#
# def remove_left(d):
#     if d:
#         d.popleft()
#
#
# commands = {
#     0: add_left,
#     1: add_right,
#     2: insert_after,
#     3: remove,
#     4: remove_all,
#     5: remove_left,
# }
#
# d = deque()
#
# while True:
#     inp = sys.stdin.readline().strip()
#     if inp == "6":
#         break
#     cmd, *args = map(int, inp.split())
#     # if cmd == 4:
#     #     d = commands[cmd](*args, d)
#     #     continue
#     commands[cmd](*args, d)
#
# for x in d:
#     print(x, end=" ")
#
#
# import sys
# from collections import deque
#
# if __name__ == '__main__':
#     d = deque()
#
#     commands = {
#         0: lambda n, d: d.appendleft(n),
#         1: lambda n, d: d.append(n),
#         2: lambda a, b, d: d.insert(d.index(a) + 1, b) if a in d else d.appendleft(b),
#         3: lambda n, d: d.remove(n) if n in d else None,
#         4: lambda n, d: [d.remove(x) for x in list(d) if x == n],
#         5: lambda d: d.popleft() if d else None,
#     }
#
#     while True:
#         inp = sys.stdin.readline().strip()
#         if inp == "6":
#             break
#         cmd, *args = map(int, inp.split())
#         commands[cmd](*args, d)
#
#     for x in d:
#          sys.stdout.write(str(x) + " ")

# from collections import deque
# import sys
#
# if __name__ == '__main__':
#     d = deque()
#
#     my_dict = {
#         '0':
#     }
#
#     while True:
#         inp = sys.stdin.readline().strip()
#         if inp == "6":
#             break
#         elif inp[0] == "3":
#             k, n = map(int, inp.split())
#             try:
#                 d.remove(n)
#             except ValueError:
#                 continue
#         elif inp[0] == "4":
#             k, n = map(int, inp.split())
#             # for x in list(d):
#             #     if x == n:
#             #         d.remove(x)
#             d = deque(x for x in d if x != n)
#         elif inp == "5":
#             if d:
#                 d.popleft()
#         elif inp[0] == "0":
#             k, n = map(int, inp.split())
#             d.appendleft(n)
#         elif inp[0] == "1":
#             k, n = map(int, inp.split())
#             d.append(n)
#         elif inp[0] == "2":
#             k, a, b = map(int, inp.split())
#             if a in d:
#                 index = d.index(a)
#                 d.insert(index + 1, b)
#             else:
#                 d.appendleft(b)
#
#     for x in d:
#         print(x, end=" ")


# from collections import deque, defaultdict
# import sys
#
# if __name__ == '__main__':
#     d = deque()
#     my_dict = defaultdict(int)
#
#     while True:
#         inp = sys.stdin.readline().strip()
#         if inp[0] == "0":
#             k, n = map(int, inp.split())
#             d.appendleft(n)
#             my_dict[n] += 1
#
#         elif inp[0] == "1":
#             k, n = map(int, inp.split())
#             d.append(n)
#             my_dict[n] += 1
#
#         elif inp[0] == "2":
#             k, a, b = map(int, inp.split())
#             if a in my_dict:
#                 d.insert(d.index(a) + 1, b)
#             else:
#                 d.appendleft(b)
#             my_dict[b] += 1
#
#         elif inp[0] == "3":
#             k, n = map(int, inp.split())
#             if n in my_dict:
#                 d.remove(n)
#                 my_dict[n] -= 1
#                 if my_dict[n] == 0:
#                     my_dict.pop(n)
#
#         elif inp[0] == "4":
#             k, n = map(int, inp.split())
#             if n in my_dict:
#                 d = deque(x for x in d if x != n)
#                 my_dict.pop(n)
#
#         elif inp == "5":
#             if d:
#                 n = d.popleft()
#                 my_dict[n] -= 1
#                 if my_dict[n] == 0:
#                     my_dict.pop(n)
#         elif inp == "6":
#             #sys.stdout.write(" ".join(map(str, d)))
#             sys.stdout.writelines(' '.join(map(str, d)))

    #print(my_dict)

# if __name__ == '__main__':
#     d = deque()
#     s = set()
#
#     while True:
#         inp = input().strip()
#         if inp == "6":
#             break
#         elif inp[0] == "3":
#             k, n = map(int, inp.split())
#             if n in s:
#                 d.remove(n)
#                 s.remove(n)
#         elif inp[0] == "4":
#             k, n = map(int, inp.split())
#             d = deque(x for x in d if x != n)
#             s.discard(n)
#         elif inp == "5":
#             if d:
#                 s.discard(d.popleft())
#         elif inp[0] == "0":
#             k, n = map(int, inp.split())
#             d.appendleft(n)
#             s.add(n)
#         elif inp[0] == "1":
#             k, n = map(int, inp.split())
#             d.append(n)
#             s.add(n)
#         elif inp[0] == "2":
#             k, a, b = map(int, inp.split())
#             if a in s:
#                 index = d.index(a)
#                 d.insert(index + 1, b)
#                 s.add(b)
#             else:
#                 d.appendleft(b)
#                 s.add(b)
#
#     for x in d:
#         print(x, end=" ")

# from collections import deque, defaultdict
# import sys
#
# if __name__ == '__main__':
#     d = deque()
#     my_dict = defaultdict(int)
#
#     while True:
#         inp = sys.stdin.readline().strip()
#         if inp[0] == "0":
#             k, n = map(int, inp.split())
#             d.appendleft(n)
#             my_dict[n] += 1
#
#         elif inp[0] == "1":
#             k, n = map(int, inp.split())
#             d.append(n)
#             my_dict[n] += 1
#
#         elif inp[0] == "2":
#             k, a, b = map(int, inp.split())
#             if a in my_dict:
#                 d.insert(d.index(a) + 1, b)
#             else:
#                 d.appendleft(b)
#             my_dict[b] += 1
#
#         elif inp[0] == "3":
#             k, n = map(int, inp.split())
#             if n in my_dict:
#                 d.remove(n)
#                 my_dict[n] -= 1
#                 if my_dict[n] == 0:
#                     my_dict.pop(n)
#
#         elif inp[0] == "4":
#             k, n = map(int, inp.split())
#             if n in my_dict:
#                 d = deque(x for x in d if x != n)
#                 my_dict.pop(n)
#
#         elif inp == "5":
#             if d:
#                 n = d.popleft()
#                 my_dict[n] -= 1
#                 if my_dict[n] == 0:
#                     my_dict.pop(n)
#         #print(my_dict)
#         elif inp == "6":
#             # sys.stdout.write(" ".join(str(x) for x in d))
#             sys.stdout.writelines(' '.join(map(str, d)))
#             break

from collections import deque, defaultdict
import sys

if __name__ == '__main__':
    d = deque()
    my_dict = defaultdict(int)

    while True:
        inp = sys.stdin.readline().strip()

        if inp[0] == "0":
            k, n = inp.split()
            d.appendleft(n)
            my_dict[n] += 1

        elif inp[0] == "1":
            k, n = inp.split()
            d.append(n)
            my_dict[n] += 1

        elif inp[0] == "2":
            k, a, b = inp.split()
            if a in my_dict:
                d.insert(d.index(a) + 1, b)
            else:
                d.appendleft(b)
            my_dict[b] += 1

        elif inp[0] == "3":
            k, n = inp.split()
            if n in my_dict:
                d.remove(n)
                my_dict[n] -= 1
                if my_dict[n] == 0:
                    my_dict.pop(n)

        elif inp[0] == "4":
            k, n = inp.split()
            if n in my_dict:
                d = deque(x for x in d if x != n)
                my_dict.pop(n)

        elif inp == "5":
            if d:
                n = d.popleft()
                my_dict[n] -= 1
                if my_dict[n] == 0:
                    my_dict.pop(n)
        #print(my_dict)
        elif inp == "6":
            break

    sys.stdout.write(" ".join(str(x) for x in d))