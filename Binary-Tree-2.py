class Node:
    def __init__ (root, data):
        root.node = data
        root.left = None
        root.right = None
        
    
def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.node, end = " ")
        Inorder(root.right)
        
def Preorder(root):
    if root:
        print(root.node, end = " ")
        Preorder(root.left)
        Preorder(root.right)

def Postorder(root):
    if root:
        Postorder(root.left)
        Postorder(root.right)
        print(root.node, end = " ")

def Level(root):
    Order = []
    Order.append(root)
    while len(Order) != 0:
        root = Order.pop(0)
        print(root.node, end = " ")
        if root.left:
            Order.append(root.left)
        if root.right:
            Order.append(root.right)

def Insert(root, userinput):
    if userinput < root.node:
        if root.left is None:
            root.left = Node(userinput)
        else:
            Insert(root.left, userinput)
    else:
        if root.right is None:
            root.right = Node(userinput)
        else:
            Insert(root.right, userinput)
    return

def Findnum(root, userinput):
    if userinput < root.node:
        if root.left:
            return Findnum(root.left, userinput)
        else:
            print(str(userinput)+" None")
    elif userinput > root.node:
        if root.right:
            return Findnum(root.right, userinput)
        else:
            print(str(userinput)+" None")
    else:
        print(str(root.node)+" Present")
        
def Remove(root, userinput):
    if not root:
        return root
    elif userinput < root.node:
        root.left = Remove(root.left, userinput)
    elif userinput > root.node:
        root.right = Remove(root.right, userinput)
        
    else:
        if not root.left and not root.right:
            root = None
        elif not root.left:
            root = root.right
        elif not root.right:
            root = root.left
        else:
            temp = root.Minimum(root.right)
            root.node = temp.node
            root.right = root.Remove(root.right,temp.node)
    return root

def Minimum(self, root):
    current = root
    while current.left:
        current = current.left
    return current
            
root = Node(35)
root.left = Node(10)
root.left.left = Node(8)
root.left.left.left = Node(5)
root.left.right = Node(18)
root.left.right.left = Node(16)
root.left.right.left.left = Node(15)
root.left.right.right = Node(29)
root.left.right.right.left = Node(28)
root.left.right.right.left.left = Node(22)

root.right = Node(75)
root.right.left = Node(40)
root.right.left.left = Node(38)
root.right.left.right = Node(45)
root.right.left.right.left = Node(43)
root.right.left.right.right = Node(50)
root.right.left.right.right.left = Node(46)
root.right.left.right.right.right = Node(55)
root.right.right = Node(83)
root.right.right.left = Node(79)
root.right.right.right = Node(85)
root.right.right.right.right = Node(92)

choice = 0
while choice != 8:
    print("\n")
    print(40*"*")
    print("\t\tMENU")
    print(40*"*")
    print("[1]Pre\n[2]In\n[3]Post\n[4]Level\n[5]Insert\n[6]Remove\n[7]Search\n[8]Exit\n")
    try:
        ans = int(input("Enter your Choice: "))
        if ans == 1:
            print("Preorder:")
            Preorder(root)
        if ans == 2:
            print("Inorder:")
            Inorder(root)
        if ans == 3:
            print("Postorder:")
            Postorder(root)
        if ans == 4:
            print("Level:")
            Level(root )
        if ans == 5:
            userinput = int(input("Enter a number: "))
            Insert(root, userinput)
            print("Updated Binary Tree:")
            Inorder(root)
        if ans == 6:
            userinput = int(input("Enter a number: "))
            Remove(root, userinput)
            print("Updated Binary Tree:")
            Inorder(root)
        if ans == 7:
            userinput = int(input("Enter a number: "))
            Findnum(root, userinput)
            print("Updated Binary Tree:")
            Inorder(root)
        if ans == 8:
            print("Exit the Program")
    except ValueError:
        print("Wrong Input")
        

        
