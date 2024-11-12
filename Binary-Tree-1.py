class Node:
    def __init__ (root, data):
        root.node = data
        root.left = None
        root.right = None

def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.node, end=" ")
        Inorder(root.right)



root = Node(60)
root.left = Node(45)
root.left.left = Node(12)
root.left.left.left = Node(10)
root.left.left.left.left = Node(3)
root.left.right = Node(53)
root.left.left.right = Node(25)
root.left.left.right.left = Node(18)
root.left.left.right.right = Node(30)
root.left.left.right.left.right = Node(20)

root.right = Node(90)
root.right.right = Node(99)
root.right.left = Node(74)
root.right.left.right = Node(84)
root.right.left.right.left = Node(82)
root.right.left.right.left.left = Node(81)

print("Sofia Joy D. Yunun")
Inorder(root)
