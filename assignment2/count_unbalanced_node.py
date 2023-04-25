import sys
from collections import deque

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # def insert(self, data):
    #     # Compare the new value with the parent node
    #     if self.data:
    #         if data < self.data:
    #             if self.left is None:
    #                 self.left = Node(data)
    #             else:
    #                 self.left.insert(data)
    #         elif data > self.data:
    #             if self.right is None:
    #                 self.right = Node(data)
    #             else:
    #                 self.right.insert(data)
    #     else:
    #         self.data = data


def insert(root, key):
    newnode = Node(key)
    curr = root
    prev = None
    if root is None:
        return newnode

    while curr:
        prev = curr
        if key == curr.data:
            return root
        elif key < curr.data:
            curr = curr.left
        else:
            curr = curr.right

    if key < prev.data:
        prev.left = newnode
    else:
        prev.right = newnode
    return root

def getHeight(node):
    if node is None:
        return 0
    return 1 + max(getHeight(node.left), getHeight(node.right))

# def getHeight(root):
#     # Base Case
#     if root is None:
#         return 0
#
#     # Create a empty queue for level order traversal
#     q = deque()
#
#     # Enqueue Root and Initialize Height
#     q.append(root)
#     height = 0
#
#     while True:
#
#         # nodeCount(queue size) indicates number of nodes
#         # at current level
#         nodeCount = len(q)
#         if nodeCount == 0:
#             return height
#
#         height += 1
#
#         # Dequeue all nodes of current level and Enqueue
#         # all nodes of next level
#         while (nodeCount > 0):
#             node = q[0]
#             q.popleft()
#             if node.left is not None:
#                 q.append(node.left)
#             if node.right is not None:
#                 q.append(node.right)
#
#             nodeCount -= 1
# def isBalanced(node):
#     if node is None:
#         return True
#     leftHeight = getHeight(node.left)
#     rightHeight = getHeight(node.right)
#     return abs(leftHeight - rightHeight) <= 1


# def countUnbalancedNodes(node):
#     if node is None:
#         return 0
#     count = 0
#     if not isBalanced(node):
#         count += 1
#     count += countUnbalancedNodes(node.left)
#     count += countUnbalancedNodes(node.right)
#     return count


def countUnbalancedNodes(node):
    if node is None:
        return 0
    count = 0
    stack = deque()
    stack.append(root)
    while stack:
        node = stack.pop()
        left_height = getHeight(node.left)
        right_height = getHeight(node.right)
        if abs(left_height - right_height) > 1:
            count += 1

        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)

    return count


if __name__ == '__main__':
    root = Node(int(sys.stdin.readline().strip()))
    while True:
        temp = sys.stdin.readline().strip()
        if temp == "":
            break
        insert(root, int(temp))
    print("So node bi mat can bang la", countUnbalancedNodes(root))


    # root = Node(int(input()))
    # for line in iter(input, ''):
    #     root.insert(int(line.strip()))
    # print("So node bi mat can bang la", countUnbalancedNodes(root))