#SOFIA JOY D. YUNUN
class Node:
    def __init__ (self, data):
        self.node = data
        self.left = None
        self.right = None

    def Inorder(self):
        if self.left:
            self.left.Inorder()
        print(self.node,end = " ")  
        if self.right:
            self.right.Inorder() 


root = Node(8)
root.left = Node(4)
root.left.left = Node(2)
root.left.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left = Node(5)
root.left.right.right = Node(7)

root.right = Node(12)
root.right.left = Node(10)
root.right.left.left = Node(9)
root.right.left.right = Node(11)
root.right.right = Node(14)
root.right.right.right = Node(15)
root.right.right.left = Node(13)

root.Inorder()
