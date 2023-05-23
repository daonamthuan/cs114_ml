# import sys
# from collections import deque
# #import queue
#
#
# class Cell:
#     def __init__(self, x, y, dist, key):
#         self.x = x
#         self.y = y
#         self.dist = dist  # distance to start
#         self.key = key
#         #self.prev = prev  # parent cell in the path
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
#         # if matrix[sx][sy] == "1" or matrix[dx][dy] == "1":
#         #     print(-1)
#         #     return
#         # initialize the cells
#         cells = deque()
#         for i in range(0, m):
#             row = deque()
#             for j in range(0, n):
#                 # if matrix[i][j] != "1":
#                 row.append(Cell(i, j, sys.maxsize, int(matrix[i][j])))
#                 # else:
#                 #     row.append(None)
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
#                 print(p.dist)
#                 break
#                 # moving up
#             self.visit(p.key, cells, queue, p.x - 1, p.y, p)
#             # moving left
#             self.visit(p.key, cells, queue, p.x, p.y - 1, p)
#             # moving down
#             self.visit(p.key, cells, queue, p.x + 1, p.y, p)
#             # moving right
#             self.visit(p.key, cells, queue, p.x, p.y + 1, p)
#             #moving right-up cross
#             self.visit(p.key, cells, queue, p.x-1, p.y+1, p)
#             #moving left-up cross
#             self.visit(p.key, cells, queue, p.x-1, p.y-1, p)
#             #moving right-down cross
#             self.visit(p.key, cells, queue, p.x+1, p.y+1, p)
#             # moving left-down cross
#             self.visit(p.key, cells, queue, p.x+1, p.y-1, p)
#             if len(queue) > 0:
#                 p = queue.popleft()
#             else:
#                 #print("+")
#                 p = None
#                 # compose the path if path exists
#         # if dest == None:
#         #     print(-1)
#         #     return
#         # else:
#         #print(dest.dist)
#             # path = []
#             # p = dest
#             # while p != None:
#             #     path.insert(0, p)
#             #     p = p.prev
#             # for i in path:
#             #     print(i, matrix[i.x][i.y])
#             #print("Distance from start to end: ", dest.dist)
#
#     # function to update cell visiting status, Time O(1), Space O(1)
#     def visit(self, key, cells, queue, x, y, parent):
#         # out of boundary
#         if x < 0 or x >= len(cells) or y < 0 or y >= len(cells[0]) or cells[x][y] == None:
#             return
#         # update distance, and previous node
#         dist = parent.dist + int(key)
#         p = cells[x][y]
#         if dist < p.dist:
#             p.dist = dist
#             #p.prev = parent
#             queue.append(p)
#
#
# if __name__ == '__main__':
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
#     # end0 = 50
#     # end1 = 51
#     myObj.shortestPath(d, (start0, start1), (end0, end1), m, n)

import heapq
import sys
from collections import deque

def dijkstra(matrix, start, end, m, n):
    # Khởi tạo một matrix lưu trữ khoảng cách ngắn nhất từ điểm bắt đầu đến các điểm khác
    dist = [[sys.maxsize for _ in range(n)] for _ in range(m)]
    # dist[start[0] * cols + start[1]] = 0

    # Khởi tạo hàng đợi ưu tiên
    heap = [(0, start)]

    # Tìm đường đi ngắn nhất
    while heap:
        (cost, node) = heapq.heappop(heap)
        r, c = node

        # Nếu đến đích thì trả về chi phí của đường đi ngắn nhất
        if node == end:
            return cost

        # Duyệt qua các điểm kề
        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                new_cost = cost + matrix[r][c]
                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    heapq.heappush(heap, (new_cost, (nr, nc)))

    # Nếu không tìm thấy đường đi, trả về None
    return None

if __name__ == '__main__':
    d = deque()
    m, n, start0, start1, end0, end1 = map(int, sys.stdin.readline().split())
    # print(m, n, start0, start1, end0, end1)
    for _ in range(m):
        temp = sys.stdin.readline().split()
        d.appendleft([int(x) for x in temp])

    distance = dijkstra(d, (start0, start1), (end0, end1), m, n)
    if distance is not None:
        print(distance)
