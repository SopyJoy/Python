class LinkedList:
    def __init__ (self):
        self.head=None

    def display(self):
        disHead = self.head
        if disHead != None:
            print("Linked List: ", disHead.data, end = ' ')
            while disHead.next != None:
                disHead = disHead.next
                print(disHead.data, end = ' ')
            
        else:
                print("Linked List is empty")
          
    def beginning(self, userinput):
        NewNode = Node(userinput)
        NewNode.next = self.head
        self.head = NewNode

    def end(self, userinput):
        NewNode = Node(userinput)
        if self.head is None:
            self.head = NewNode
            return
        lastnode = self.head
        while(lastnode.next):
            lastnode = lastnode.next
        lastnode.next = NewNode

    def length(self):
        cur = self.head
        total = 1
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    
    def between(self, userinput):
        half = ll.length() // 2
        NewNode = Node(userinput)
        if self.head is None:
            self.head = NewNode
            return
        midnode = self.head
        for x in range(half-1):
            midnode = midnode.next
        NewNode.next = midnode.next
        midnode.next = NewNode

    def delete(self, userinput):
        delnode = self.head
        
        #for the first data to ensure it doesnt cause an error
        if (delnode.data.lower() == userinput.lower()):
            self.head = delnode.next
            delnode = None
            return
        
        while(delnode is not None):
            if (delnode.data.lower() == userinput.lower()):
                prev.next = delnode.next
                delnode = None
                break
            if (delnode != None):
                prev = delnode
                delnode = delnode.next
        
         
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
ll = LinkedList()       
first= Node("Red")
second = Node("Brown")
third = Node("Orange")
fourth = Node("White")
fifth = Node("Green")
sixth = Node("Yellow")
seventh = Node("Purple")
eight = Node("Blue")
nine = Node("Pink")
ll.head = Node("Black")

ll.head.next = eight
eight.next = second
second.next = fifth
fifth.next = third
third.next = nine
nine.next = seventh
seventh.next = first
first.next = fourth
fourth.next = sixth


choice = 0
while choice != 6:
    print("\nMENU")
    print("[1] Begin\n[2] End\n[3] In Between\n[4] Display\n[5] Delete\n[6] Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            userinput = input("Enter your color: ")
            ll.beginning(userinput)
            ll.display()
        elif choice == 2:
            userinput = input("Enter your color: ")
            ll.end(userinput)
            ll.display()
        elif choice == 3:
            userinput = input("Enter your color: ")
            ll.between(userinput)
            ll.display()
        elif choice == 4:
            ll.display()
        elif choice == 5:
            userinput = input("Enter your color: ")
            ll.delete(userinput)
            ll.display()
        elif choice == 6:
            print("End of Program")
        else:
            print("Wrong Input!")
    except ValueError:
        print("Wrong Input!")


                    


