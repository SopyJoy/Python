class LinkedList:
    def __init__ (self):
        self.head = None
        
    def display(self):
        Head = self.head
        if Head != None:
            print(Head.data," : ",end=" ")
            while Head.next != None:
                Head = Head.next
                print(Head.data, end=" ")
        else:
            print("Linked List is Empty")
        

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

ll = LinkedList()

ll.head = Node("FRUITS")
F1 = Node("Kiwi")
F2 = Node("Grapes")
F3 = Node("Pineapple")
F4 = Node("Banana")
F5 = Node("Watermelon")
F6 = Node("Apple")
F7= Node("Strawberry")
F8 = Node("Jackfruit")
F9 = Node("Cherry")
F10 = Node("Orange")

ll.head.next = F6
F6.next = F4
F4.next = F9
F9.next = F2
F2.next = F8
F8.next = F1
F1.next = F10
F10.next = F3
F3.next = F7
F7.next = F5

print("Sofia Joy D. Yunun")
ll.display()
