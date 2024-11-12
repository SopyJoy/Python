def add():
    add = input("Enter a value: ")
    UserList.append(add)
    if len(UserList) <=5:
        print("Current Stack: ", UserList)
        print("Stack Top Item: ", UserList[-1])
        print("Stack Length: ", len(UserList))
    else:
        print("WARNING: Overflow!!")

    
def sub():
    try:
        UserList.pop()
        if len(UserList) > 0:
            print("Current Stack: ", UserList)
            print("Stack Top Item: ",UserList[-1])
            print("Stack Length: ", len(UserList))
        else:
            print("WARNING: Underflow!!")
    except IndexError:
        print("WARNING: Underflow!!Empty List")
    
def exitProgram():
    print("EDI DONT ( ͡👁️ ʖ ͡👁️)")
    

UserList =[]
user = 0
while user !=3:
    print(40*"*","\n\t\tMENU")
    print(40*"*")
    print("\n[1] Push\n[2] Pop\n[3] Exit")
    try:
        user = int(input("\nEnter your Choice number: "))
        if user == 1:
            add()
        if user == 2:
            sub()
        if user == 3:
            exitProgram()
    except ValueError:
        print("Wroing Input, Please Try Again. ( ͡👁️ ㅅ ͡👁️)")   
     


