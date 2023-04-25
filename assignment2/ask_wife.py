# # import heapq
# # from collections import deque
# # import sys
# #
# #
# # def dijkstra(graph, start, end):
# #     heap = [(0, start)]
# #     visited = set()
# #     while heap:
# #         (cost, current) = heapq.heappop(heap)
# #         if current in visited:
# #             continue
# #         visited.add(current)
# #         if current == end:
# #             return cost
# #         for neighbor, weight in graph[current].items():
# #             if neighbor not in visited:
# #                 heapq.heappush(heap, (cost + weight, neighbor))
# #     return -1
# #
# #
# # def shortest_path(matrix, start, end):
# #     rows, cols = len(matrix), len(matrix[0])
# #     graph = {i * cols + j: {} for i in range(rows) for j in range(cols)}
# #     for i in range(rows):
# #         for j in range(cols):
# #             if matrix[i][j] != "#":
# #                 if j < cols - 1 and matrix[i][j+1] != "#":
# #                     graph[i*cols+j][i*cols+j+1] = 1
# #                     graph[i*cols+j+1][i*cols+j] = 1
# #                 if i < rows - 1 and matrix[i+1][j] != "#":
# #                     graph[i*cols+j][(i+1)*cols+j] = 1
# #                     graph[(i+1)*cols+j][i*cols+j] = 1
# #     start_node = start[0] * cols + start[1]
# #     end_node = end[0] * cols + end[1]
# #     return dijkstra(graph, start_node, end_node)
#
# import sys
# from collections import deque
# import queue
#
#
# class Cell:
#     def __init__(self, x, y, dist):
#         self.x = x
#         self.y = y
#         self.dist = dist  # distance to start
#         #self.prev = prev  # parent cell in the path
#
#     # def __str__(self):
#     #     return "(" + str(self.x) + "," + str(self.y) + ")"
#
#
# class ShortestPathBetweenCellsBFS:
#     # BFS, Time O(n^2), Space O(n^2)
#     def shortestPath(self, matrix, start, end):
#         sx = start[0]
#         sy = start[1]
#         dx = end[0]
#         dy = end[1]
#         # if start or end value is 0, return
#         if matrix[sx][sy] == 1 or matrix[dx][dy] == 1:
#             print("-1")
#             return
#         # initialize the cells
#         m = len(matrix)
#         n = len(matrix[0])
#         cells = []
#         for i in range(0, m):
#             row = []
#             for j in range(0, n):
#                 if matrix[i][j] != '1':
#                     row.append(Cell(i, j, sys.maxsize))
#                 else:
#                     row.append(None)
#             cells.append(row)
#             # breadth first search
#         # print("============")
#         # for x in cells:
#         #     print()
#         # print("============")
#         queue = []
#         src = cells[sx][sy]
#         src.dist = 0
#         queue.append(src)
#         dest = None
#         p = queue.pop(0)
#         while p != None:
#             # find destination
#             if p.x == dx and p.y == dy:
#                 dest = p
#                 break
#                 # moving up
#             self.visit(cells, queue, p.x - 1, p.y, p, matrix)
#             # moving left
#             self.visit(cells, queue, p.x, p.y - 1, p, matrix)
#             # moving down
#             self.visit(cells, queue, p.x + 1, p.y, p, matrix)
#             # moving right
#             self.visit(cells, queue, p.x, p.y + 1, p, matrix)
#             print("------------")
#             if len(queue) > 0:
#                 p = queue.pop(0)
#             else:
#                 p = None
#                 # compose the path if path exists
#         if dest == None:
#             print("-1")
#             return
#         else:
#             print(dest.dist)
#             # path = []
#             # p = dest
#             # while p != None:
#             #     path.insert(0, p)
#             #     p = p.prev
#             # for i in path:
#             #     print(i)
#
#     # function to update cell visiting status, Time O(1), Space O(1)
#     def visit(self, cells, queue, x, y, parent, matrix):
#         # out of boundary
#         if x < 0 or x >= len(cells) or y < 0 or y >= len(cells[0]) or matrix[x][y] == '1':
#             return
#         # update distance, and previous node
#         dist = parent.dist + 1
#         p = cells[x][y]
#         if dist < p.dist:
#             p.dist = dist
#             #p.prev = parent
#             queue.append(p)
#             print(p.x, p.y, matrix[x][y])
#
# #
# # matrix = [
# #     [1, 0, 1],
# #     [0, 1, 1],
# #     [0, 0, 1]]
# # myObj = ShortestPathBetweenCellsBFS()
# # # case1, there is no path
# # start = [0, 0]
# # end = [1, 1]
# # print("case 1: ")
# # myObj.shortestPath(matrix, start, end)
# # # case 2, there is path
# # start1 = [0, 2]
# # end1 = [1, 1]
# # print("case 2: ")
# # myObj.shortestPath(matrix, start1, end1)
#
#
# if __name__ == '__main__':
#     d = deque()
#     m, n, start0, start1, end0, end1 = map(int, sys.stdin.readline().split())
#     # print(m, n, start0, start1, end0, end1)
#     for _ in range(m):
#         d.appendleft(sys.stdin.readline().split())
#
#     myObj = ShortestPathBetweenCellsBFS()
#     myObj.shortestPath(d, (start0, start1), (end0, end1))
#     # print(d)
#     # for x in d:
#     # print(x)

#
# import sys
# from collections import deque
#
#
# class Cell:
#     def __init__(self, x, y, dist):
#         self.x = x
#         self.y = y
#         self.dist = dist  # distance to start
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
#         if matrix[sx][sy] == "1" or matrix[dx][dy] == "1":
#             print(-1)
#             return
#         # initialize the cells
#         cells = deque()
#         for i in range(0, m):
#             row = deque()
#             for j in range(0, n):
#                 if matrix[i][j] != "1":
#                     row.append(Cell(i, j, sys.maxsize))
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
#             # moving right
#             self.visit(cells, queue, p.x, p.y + 1, p)
#             #moving top-right
#             self.visit(cells, queue, p.x-1, p.y+1, p)
#             #moving top-left
#             self.visit(cells, queue, p.x-1, p.y-1, p)
#             #moving bot-right
#             self.visit(cells, queue, p.x+1, p.y+1, p)
#             # moving bot-left
#             self.visit(cells, queue, p.x+1, p.y-1, p)
#             if len(queue) > 0:
#                 p = queue.popleft()
#             else:
#                 p = None
#         # compose the path if path exists
#         if dest is not None:
#             print(dest.dist)
#         else:
#             print(-1)
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
#     def visit(self, cells, queue, x, y, parent):
#         # out of boundary
#         if x < 0 or x >= len(cells) or y < 0 or y >= len(cells[0]) or cells[x][y] == None:
#             return
#         # update distance, and previous node
#         dist = parent.dist + 1
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
#     # end0 = 51
#     # end1 = 51
#     myObj.shortestPath(d, (start0, start1), (end0, end1), m, n)
#     #print("Shortest path from start to end: {}".format(dest.dist))

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
        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] == 0:
                new_cost = cost + 1
                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    heapq.heappush(heap, (new_cost, (nr, nc)))

    # Nếu không tìm thấy đường đi, trả về None
    return -1

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