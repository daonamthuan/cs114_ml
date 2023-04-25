#
# import sys
# from collections import deque
#
#
# class Cell:
#     def __init__(self, x, y, dist, prev):
#         self.x = x
#         self.y = y
#         self.dist = dist  # distance to start
#         self.prev = prev  # parent cell in the path
#
#
# class ShortestPathBetweenCellsBFS:
#     # BFS, Time O(n^2), Space O(n^2)
#     def shortestPath(self, matrix, start, end, m, n):
#         sx = start[0]
#         sy = start[1]
#         dx = end[0]
#         dy = end[1]
#         # if start or end value is 0, return
#         if matrix[sx][sy] == "1" or matrix[dx][dy] == "1":
#             print(-1)
#             return
#         # initialize the cells
#         cells = deque()
#         for i in range(0, m):
#             row = deque()
#             for j in range(0, n):
#                 if matrix[i][j] != "1":
#                     row.append(Cell(i, j, sys.maxsize, None))
#                 else:
#                     row.append(None)
#             cells.append(row)
#             # breadth first search
#         queue = deque()
#         src = cells[sx][sy]
#         src.dist = 0
#         queue.append(src)
#         dest = None
#         p = queue.popleft()
#         while p != None:
#             # find destination
#             if p.x == dx and p.y == dy:
#                 dest = p
#                 # break
#                 # moving up
#             self.visit(cells, queue, p.x - 1, p.y, p)
#             # moving left
#             self.visit(cells, queue, p.x, p.y - 1, p)
#             # moving down
#             self.visit(cells, queue, p.x + 1, p.y, p)
#             #moving right
#             self.visit(cells, queue, p.x, p.y + 1, p)
#             # #moving top-right
#             # self.visit(cells, queue, p.x-1, p.y+1, p)
#             # #moving top-left
#             # self.visit(cells, queue, p.x-1, p.y-1, p)
#             # #moving bot-right
#             # self.visit(cells, queue, p.x+1, p.y+1, p)
#             # # moving bot-left
#             # self.visit(cells, queue, p.x+1, p.y-1, p)
#             if len(queue) > 0:
#                 p = queue.popleft()
#             else:
#                 p = None
#         # compose the path if path exists
#         if dest is None:
#             print(-1)
#         else:
#             # print(-1)
#             path = deque()
#             p = dest
#             while p != None:
#                 path.appendleft(p)
#                 p = p.prev
#             for i in path:
#                 print(i.x, i.y, matrix[i.x][i.y])
#             print("Number of drift: ", self.drift(path))
#             print("Distance from start to end: ", dest.dist)
#
#     # function to update cell visiting status, Time O(1), Space O(1)
#     def visit(self, cells, queue, x, y, parent):
#         # out of boundary
#         if x < 0 or x >= len(cells) or y < 0 or y >= len(cells[0]) or cells[x][y] == None:
# #             return
# #         # update distance, and previous node
# #         dist = parent.dist + 1
# #         p = cells[x][y]
# #         if dist < p.dist:
# #             p.dist = dist
# #             p.prev = parent
# #             queue.append(p)
# #
# #     def drift(self, path):
#         num_drift = 0
#         # p = path[-1]
#         # while p:
#         #     prev1 = p.prev
#         #     prev2 = prev1.prev
#         #
#         #     if prev2 is None:
#         #         return num_drift
#         #     if prev2.y == prev1.y and p.y != prev1.y:
#         #         num_drift += 1
#         #     elif prev2.x == prev1.x and p.x != prev1.x:
#         #         num_drift += 1
#         #
#         #     p = p.prev
# #
# #         return num_drift
# #
# #
# #
# # if __name__ == '__main__':
#     d = deque()
#     m, n, start0, start1, end0, end1 = map(int, sys.stdin.readline().split())
#     # print(m, n, start0, start1, end0, end1)
#     for _ in range(m):
#         d.appendleft(sys.stdin.readline().split())
#     # for x in d:
#     #     print(x)
#     myObj = ShortestPathBetweenCellsBFS()
#     # start = [start0, start1]
#     # end = [end0, end1]
#     #print("case 1: ")
#     # start0 = 0
#     # start1 = 2
#     # end0 = 51
#     # end1 = 51
#     myObj.shortestPath(d, (start0, start1), (end0, end1), m, n)

import heapq
import sys
from collections import deque


class Node:
    def __init__(self, x, y, dist, prev):
        self.x = x
        self.y = y
        self.dist = dist
        self.prev = prev


def dijkstra(matrix, start, end, m, n):
    # Khởi tạo một matrix lưu trữ khoảng cách ngắn nhất từ điểm bắt đầu đến các điểm khác
    # dist = [[sys.maxsize for _ in range(n)] for _ in range(m)]
    # lst = [[Node() for _ in range(n)] for _ in range(m)]
    cells = deque()
    for i in range(0, m):
        row = deque()
        for j in range(0, n):
            row.append(Node(i, j, sys.maxsize, None))
        cells.append(row)

    # Khởi tạo hàng đợi ưu tiên
    heap = [(0, start)]

    # Tìm đường đi ngắn nhất
    while heap:
        (cost, node) = heapq.heappop(heap)
        r, c = node

        # Numbers of drift
        if node == end:
            print("Cost: ", cost)
            # path = deque()
            p = cells[r][c]
            # while p:
            #     print("{},{}".format(p.x, p.y))
            #     path.appendleft(p)
            #     p = p.prev
            # # for i in path:
            # #     print(i)
            # p = path[-1]
            num_drift = 0
            while p:
                print("======")
                prev1 = p.prev
                prev2 = prev1.prev

                if prev2 is None:
                    return num_drift
                if prev2.y == prev1.y and p.y != prev1.y:
                    num_drift += 1
                elif prev2.x == prev1.x and p.x != prev1.x:
                    num_drift += 1
                print("Numbers of drift: ", num_drift)

                p = p.prev
            print("Numbers of drift: ", num_drift)

        # Duyệt qua các điểm kề
        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            matrix[r][c] = 1
            nr, nc = r + dr, c + dc
            # val = matrix[nr][nc]
            if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] == 0:
                new_cost = cost + 1
                if new_cost < cells[nr][nc].dist:
                    # matrix[nr][nc] = 1
                    cells[nr][nc].dist = new_cost
                    cells[nr][nc].prev = cells[r][c]
                    heapq.heappush(heap, (new_cost, (nr, nc)))

    # Nếu không tìm thấy đường đi, trả về None
    return None


if __name__ == '__main__':
    d = deque()
    m, n, start0, start1, end0, end1 = map(int, sys.stdin.readline().split())
    for _ in range(m):
        temp = sys.stdin.readline().split()
        d.appendleft([int(x) for x in temp])
    dijkstra(d, (start0, start1), (end0, end1), m, n)

    # dist, path = dijkstra(d, (start0, start1), (end0, end1), m, n)
    # print(dist)
    # print(path)
