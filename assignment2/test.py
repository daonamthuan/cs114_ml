# # # while True:
# # #     line = input().strip()
# # #     if (line == '0'):
# # #         break
# # #     a, b = map(int, line.split())
# # #     if a == 0:
# # #         print("0")
# # #     elif a == 1:
# # #         print("11111111")
# # #     elif a == 2:
# # #         print('3')
# # #     elif a == 3:
# # #         print("4")
# # #
# # # from collections import deque
# # # import time
# # # import sys
# # #
# # # d = deque()
# # #
# # # for i in range (1000000):
# # #     d.append(i)
# # #
# # # start = time.time()
# # # #for x in d:
# # #     #print(x, end=" ")
# # # # sys.stdout.write(" ".join(map(str, d)))
# # # sys.stdout.write(" ".join(str(x) for x in d))
# # # print("Thoi gian: ", time.time() - start)
# # #
# # # for x in deque[2:5]:
# # #     print(x)
# #
# # # lst = []
# # # for i in range (5):
# # #     lst.append((i, i**2))
# # #
# # # print(lst)
# # # print(lst[4][1])
# # # for x in lst:
# # #     print(x)
# # #
# # # my_dict = {
# # #     'V': [('S', '10'), ('HA', '7'), ('Z', '10'), ('G', '1')],
# # #     'Z': [('G', '-2'), ('K', '2'), ('DA', '-10'), ('O', '-3')],
# # #     'K': [('V', '3'), ('O', '9')],
# # #     'O': [('S', '-2'), ('DA', '9'), ('HA', '-9')],
# # #     'G': [('DA', '8'), ('K', '1'), ('O', '-8')],
# # #     'S': [('K', '5')],
# # #     'DA': [('S', '7'), ('HA', '1'), ('F', '9')],
# # #     'F': [('G', '-10'), ('Z', '-4'), ('K', '7'), ('W', '8'), ('S', '0')],
# # #     'W': [('V', '5'), ('G', '10'), ('K', '8')],
# # #     'HA': [('K', '-1'), ('G', '-10'), ('Z', '-4'), ('W', '-6')],
# # # }
# # #
# # # print('V' in my_dict['K'].values())
# #
# # # from collections import deque
# # #
# # # d = deque()
# # #
# # # for i in range(11):
# # #     d.append((i, i**2))
# # #
# # # print(d)
# # # print(d[9][1])
# #
# # import heapq
# # from collections import deque
# # import sys
# #
# # dist = []
# #
# #
# # def dijkstra(matrix, start, end):
# #     global dist
# #     # Tính số hàng và số cột của ma trận
# #     rows = len(matrix)
# #     cols = len(matrix[0])
# #
# #     # Khởi tạo một mảng lưu trữ khoảng cách ngắn nhất từ điểm bắt đầu đến các điểm khác
# #     dist = [float('inf')] * (rows * cols)
# #     dist[start[0] * cols + start[1]] = 0
# #
# #     # Khởi tạo hàng đợi ưu tiên
# #     heap = [(0, start)]
# #
# #     # Tìm đường đi ngắn nhất
# #     while heap:
# #         (cost, node) = heapq.heappop(heap)
# #         r, c = node
# #
# #         # Nếu đến đích thì trả về chi phí của đường đi ngắn nhất
# #         if node == end:
# #             return cost
# #
# #         # Duyệt qua các điểm kề
# #         for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
# #             nr, nc = r + dr, c + dc
# #             if 0 <= nr < rows and 0 <= nc < cols:
# #                 new_cost = cost + int(matrix[nr][nc])
# #                 if new_cost < dist[nr * cols + nc]:
# #                     dist[nr * cols + nc] = new_cost
# #                     heapq.heappush(heap, (new_cost, (nr, nc)))
# #
# #     # Nếu không tìm thấy đường đi, trả về None
# #     return -1
# #
# #
# # if __name__ == '__main__':
# #     d = deque()
# #     m, n, start0, start1, end0, end1 = map(int, sys.stdin.readline().split())
# #     # print(m, n, start0, start1, end0, end1)
# #     for _ in range(m):
# #         d.append(sys.stdin.readline().split())
# #
# #     start = (start0, start1)
# #     end = (end0, end1)
# #     result = dijkstra(d, start, end)
# #     print(dist)
# #     print(result)
#
# from collections import deque
# import sys
#
#
# # To store matrix cell coordinates
# class Point:
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y
#
#
# # A data structure for queue used in BFS
# class queueNode:
#     def __init__(self, pt: Point, dist: int):
#         self.pt = pt  # The coordinates of the cell
#         self.dist = dist  # Cell's distance from the source
#
#
# # Check whether given cell(row,col)
# # is a valid cell or not
# def isValid(row: int, col: int, m, n):
#     return (row >= 0) and (row < m) and (col >= 0) and (col < n)
#
#
# # These arrays are used to get row and column
# # numbers of 4 neighbours of a given cell
# rowNum = [-1, 0, 0, 1, -1, -1, 1, 1]
# colNum = [0, -1, 1, 0, -1, 1, -1, 1]
#
#
# # Function to find the shortest path between
# # a given source cell to a destination cell.
# def BFS(mat, src: Point, dest: Point, m, n):
#     # check source and destination cell
#     # of the matrix have value 1
#     if mat[src.x][src.y] == "1" or mat[dest.x][dest.y] == "1":
#         return -1
#
#     visited = [[False for i in range(n)]
#                for j in range(m)]
#
#     # Mark the source cell as visited
#     visited[src.x][src.y] = True
#
#     # Create a queue for BFS
#     q = deque()
#
#     # Distance of source cell is 0
#     s = queueNode(src, 0)
#     q.append(s)  # Enqueue source cell
#
#     # Do a BFS starting from source cell
#     while q:
#
#         curr = q.popleft()  # Dequeue the front cell
#
#         # If we have reached the destination cell,
#         # we are done
#         pt = curr.pt
#         if pt.x == dest.x and pt.y == dest.y:
#             return curr.dist
#
#         # Otherwise enqueue its adjacent cells
#         for i in range(8):
#             row = pt.x + rowNum[i]
#             col = pt.y + colNum[i]
#
#             # if adjacent cell is valid, has path
#             # and not visited yet, enqueue it.
#             if (isValid(row, col, m, n) and mat[row][col] == "0" and not visited[row][col]):
#                 visited[row][col] = True
#                 Adjcell = queueNode(Point(row, col),
#                                     curr.dist + 1)
#                 q.append(Adjcell)
#
#     # Return -1 if destination cannot be reached
#     return -1
#
#
# # Driver code
#
# if __name__ == '__main__':
#     d = deque()
#     m, n, start0, start1, end0, end1 = map(int, sys.stdin.readline().split())
#     # print(m, n, start0, start1, end0, end1)
#     for _ in range(m):
#         d.appendleft(sys.stdin.readline().split())
#
#     start0 = 0
#     start1 = 2
#     end0 = 0
#     end1 = 2
#     source = Point(start0, start1)
#     dest = Point(end0, end1)
#
#     dist = BFS(d, source, dest, m, n)
#
#     print(dist)
#

# hỏi vợ
# import sys
# import queue
#
# m, n, pos_k_x, pos_k_y, pos_q_x, pos_q_y = map(int, sys.stdin.readline().split())
#
# matrix = []
#
# for _ in range(m):
#     row = list(map(int, sys.stdin.readline().split()))
#     matrix.insert(0, row)
#
# def findPath():
#     dx = [-1, 1, 0, 0, -1, 1, -1, 1]
#     dy = [0, 0, -1, 1, 1, 1, -1, -1]
#     q = queue.Queue()
#     ans = 0
#     q.put((pos_k_x, pos_k_y))
#     matrix[pos_k_x][pos_k_y] = 1
#
#     while not q.empty():
#         size = q.qsize()
#         while size > 0:
#             t = q.get()
#             for idx in range(8):
#                 currx = t[0] + dx[idx]
#                 curry = t[1] + dy[idx]
#                 if currx == pos_q_x and curry == pos_q_y:
#                     return ans + 1
#                 if 0 <= currx < m and 0 <= curry < n and matrix[currx][curry] == 0:
#                     q.put((currx, curry))
#                     matrix[currx][curry] = 1
#             size -= 1
#         ans += 1
#
#     return -5
#
#
# print(findPath())

m = 5
n = 4
lst = [[[] for i in range(n)] for j in range(m)]
print(lst)
# for x in lst:
#     print(x)