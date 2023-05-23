# define 1 node in BST
class Node:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

    # def print(self):
    #     # if there is no left_child then don't print
    #     if self.left:
    #         self.left.print()
    #     print(self.key)
    #     # if there is no left_child then don't print
    #     if self.right:
    #         self.right.print()


def add(root, num):
    if root is None:
        return Node(num)
    elif num < root.key:
        root.left = add(root.left, num)
    elif num > root.key:
        root.right = add(root.right, num)

    return root


def findnum(root, input_number):
    if root is None:
        return False

    if input_number == root.key:
        return True
    elif input_number < root.key:
        return findnum(root.left, input_number)
    else:
        return findnum(root.right, input_number)


# def minNode(node):
#     current = node
#     while current.left is not None:
#         current = current.left
#     return current


def deleteNode(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    elif key == root.key:
        # if left_child or (and) right_child is None
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # if root has both left and right child. Choose the leftmost node of the right branch
        temp = root.right
        while temp.left is not None:
            temp = root.left

        root.key = temp.key

        # delete the inorder successor
        root.right = deleteNode(root.right, temp.key)

    return root


if __name__ == '__main__':
    root = None
    res = []
    # while True:
    #     inp = input().strip()
    #     if inp == "0":
    #         break
    #     a, b = map(int, inp.split())
    #     if a == 1:
    #         root = add(root, b)
    #     elif a == 2:
    #         if findnum(root, b):
    #             res.append(1)
    #         else:
    #             res.append(0)
    #     elif a == 3:
    #         if findnum(b):
    #             root = deleteNode(root, b)




    root = add(root, 8)
    # print(root.left is None)
    # print(root.right is None)
    root = add(root, 3)
    root = add(root, 1)
    root = add(root, 6)
    root = add(root, 7)
    root = add(root, 10)
    root = add(root, 14)
    root = add(root, 4)
    print(findnum(root, 9))
    # root.print()
    for x in res:
        print(x)