def enq():
    global rear
    global front
    add = input("Enter a value: ")
    if len(UserList) <= 5:
        rear += 1
        UserList.append(add)
        print("Current List: ",UserList)
        print("Front Item: ", UserList[0])
        print("Front Index: ", front)
        print("Rear Item: ", UserList[-1])
        print("Rear Index: ", rear)
    else:
        print("WARNING: FULL")

def deq():
    global rear
    global front
    try:
        UserList.pop()
        front +=1
        if len(UserList) > 0:
            print("Current List: ",UserList)
            print("Front Item: ", UserList[0])
            print("Front Index: ", front)
            print("Rear Item: ", UserList[-1])
            print("Rear Index: ", rear)
        else:
            print("WARNING: EMPTY")
    except IndexError:
        print("WARNING: EMPTY")
    
def peak():
    print(40*"-")
    print("\t\tOPTIONS")
    print(40*"-")
    print("[a]Front\n[b]Rear")
    try:
        ans = input("Enter your choice letter: ")
        ans.lower()
        if ans == 'a':
            print("Front Item: ", UserList[0])
        if ans == 'b':
            print("Rear Item: ", UserList[-1])
    except ValueError:
        print("Please enter a correct choice letter.")
    except IndexError:
        print("Please Enqueue and Dequeue First.")
        
def exitP():
    print("Okay Thank you for your time.")

UserList=[]
user = 0
rear = -1
front = 0
while user !=4:
    try:
        print(40*"*")
        print("\t\tMENU")
        print(40*"*")
        print("[1]Enqueue\n[2]Dequeue\n[3]Peak\n[4]Exit")
        user = int(input("Enter your choice number: "))
        if user == 1:
            enq()
        if user == 2:
            deq()
        if user == 3:
            peak()
        if user == 4:
            exitP()
    except ValueError:
        print("Please enter a correct choice number.")
