# import sys
#
# def binarySearch(a, x):
#     left = 0
#     right = len(a) - 1
#     mid = 0
#     while left <= right:
#         mid = (left + right) // 2
#         if x > a[mid]:
#             left = mid + 1
#         elif x < a[mid]:
#             right = mid - 1
#         else:
#             return mid
#     if right < 0:
#         return left
#     elif left > len(a) - 1:
#         return right
#     return right if abs(a[right] - x) < abs(a[left] - x) else left
#
#
# def kNearestNumber(a, k, x, idx):
#     #res = [a[idx]]
#     count, i, j = 1, idx - 1, idx + 1
#     #print(n)
#     while count < k:
#         if i < 0:
#             j += 1
#             count += 1
#         elif j >= n:
#             i -= 1
#             count += 1
#         elif abs(a[i] - x) <= abs(a[j] - x):
#             i -= 1
#             count += 1
#         elif abs(a[i] - x) > abs(a[j] - x):
#             j += 1
#             count += 1
#     return i + 1, j - 1
#
#
# if __name__ == "__main__":
#     n = int(sys.stdin.readline())
#     a = [int(x) for x in sys.stdin.readline().split()]
#     #temp, result = [], []
#
#     while True:
#         inp = sys.stdin.readline().strip()
#         if inp == "":
#             break
#         else:
#             k, x = map(int, inp.split())
#             idx = binarySearch(a, x)
#             left, right = kNearestNumber(a, k, x, idx)
#             # #result.append(temp)
#             #print("---", result, "---", status)
#             # if status == 1:
#             #     #print(result)
#             #     #print(status)
#             #     lst = " ".join(str(x) for x in a[left:right])
#             #     print(lst)
#             # else:
#             #
#             print(a[left], a[right])
#
#     # for i in range(len(result)):
#     #     if stt[i] == 1:
#     #         str = " ".join([str(x) for x in result[i]])
#     #         print(str)
#     #     else:
#     #         print(result[i][0], result[i][-1])

import bisect

def SoGan_X(lst, x):
    i = bisect.bisect_left(lst, x)
    return i


def K_SoGan_X(k, x, lst):
    lst_result = []
    pos = SoGan_X(lst, x)

    # nhỏ hơn hoặc bằng giá trị đầu tiên
    if pos == 0:
        return lst[0:k]
    # lớn hơn giá trị cuối cùng
    elif pos >= len(lst) - 1:
        return lst[len(lst) - k:len(lst)]
    else:
        l = pos
        r = pos + 1
        # gán giá trị đầu tiên gần =x hoặc gần x nhất
        if lst[pos] == x or x - lst[l] <= lst[r] - x:
            lst_result.append(lst[pos])
            l -= 1
        else:
            lst_result.append(lst[pos + 1])
            r += 1
        count = 1

        while (count != k):
            if l < 0 and r < len(lst) - 1:  # append từ bên trái qua
                lst_result.append(lst[r])
                r += 1
            elif r > len(lst) - 1 and l >= 0:  # append từ bên phải qua
                lst_result.append(lst[l])
                l -= 1
            else:  # so sánh bên nào nhỏ thì append
                if x - lst[l] <= lst[r] - x:
                    lst_result.append(lst[l])
                    l -= 1
                else:
                    lst_result.append(lst[r])
                    r += 1
            count += 1
    return lst_result


a = input()
lst = list(map(int, input().split()))

while True:
    b = list(map(int, input().split()))
    if len(b) == 0:
        break
    else:
        result = sorted(K_SoGan_X(b[0], b[1], lst))
        print(result[0], result[-1])
