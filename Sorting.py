def bubble_asc(lst):
    print("Original List: ", lst)
    loop = 0
    num_false = 1
    while num_false != 7: #the loop will stop if there were no swaps that occured 
        num_false = 1
        print("Loop", loop)
        for ind in range(len(lst)-1):
            cur = lst[ind]
            nxt = lst[ind+1]
            print(lst)
            if cur > nxt: #Swapping Values
                temp= lst[ind]
                lst[ind] = lst[ind+1]
                lst[ind+1] = temp
            else: #Adds 1 to num_false if there was no swap
                num_false += 1
           
        print("NEW", lst)
        loop += 1

def bubble_desc(lst):
    print("Original List: ", lst)
    loop = 0
    num_false = 1
    while num_false != 7:#the loop will stop if there were no swaps that occured 
        num_false = 1
        print("Loop", loop)
        for ind in range(len(lst)-1):
            cur = lst[ind]
            nxt = lst[ind+1]
            print(lst)
            if cur < nxt: #Swapping Values
                temp= lst[ind]
                lst[ind] = lst[ind+1]
                lst[ind+1] = temp
            else: #Adds 1 to num_false if there was no swap
                num_false += 1
           
        print("NEW", lst)
        loop += 1

def sel_asc(lst):
    print("Original List: ", lst)
    loop = 0
    index_min = 0
    while loop != 7:
        min_val = lst[index_min]
        check = False
           
        for ind in range(index_min, len(lst)-1):
            nxt = lst[ind+1]
            
            #saving the values for the swap later
            if min_val > nxt:
                min_val  = nxt
                nxt_ind = ind+1
                check = True #to see if min_val is changed (if not, the swap will not happen in the code below)
                
            #swap will happen in the last iteration and if check is True
            if ind+1 == 6 and check:
                temp = lst[index_min]
                lst[index_min] = min_val
                lst[nxt_ind] = temp
                    
        print("Loop", loop, lst)
        index_min += 1
        loop += 1


def sel_desc(lst):
    print("Original List: ", lst)
    loop = 0
    index_min = 0
    while loop != 7:
        min_val = lst[index_min]
        check = False
           
        for ind in range(index_min, len(lst)-1):
            nxt = lst[ind+1]
            
            #saving the values for the swap later
            if min_val < nxt:
                min_val  = nxt
                nxt_ind = ind+1
                check = True #to see if min_val is changed (if not, the swap will not happen in the code below)
                
            #swap will happen in the last iteration and if check is True
            if ind+1 == 6 and check:
                temp = lst[index_min]
                lst[index_min] = min_val
                lst[nxt_ind] = temp
                    
        print("Loop", loop, lst)
        index_min += 1
        loop += 1
        


def insert_asc(lst):
    sort_list = []
    unsort_list = lst.copy()
    loop = -1
    for ind in range(len(lst)):
        if  len(sort_list) == 0:
            sort_list.append(lst[ind])
            unsort_list.pop(0)
            print("Original List: ", lst)
        else:
            print("Loop ", loop)
            print(sort_list + unsort_list)
            sort_list.append(lst[ind])
            unsort_list.pop(0)
            for sortlist_ind in range(-1, -len(sort_list), -1):
                cur = sort_list[sortlist_ind]
                nxt = sort_list[sortlist_ind-1]
                print(sort_list)
                if cur < nxt:
                    temp = sort_list[sortlist_ind]
                    sort_list[sortlist_ind] = sort_list[sortlist_ind-1]
                    sort_list[sortlist_ind-1] = temp
                else:
                    break
                
        loop += 1
    print("Final Sorted List: ", sort_list)
    return sort_list
        
def insert_dec(lst):
    sort_list = []
    unsort_list = lst.copy()
    loop = -1
    for ind in range(len(lst)):
        if  len(sort_list) == 0:
            sort_list.append(lst[ind])
            unsort_list.pop(0)
            print("Original List: ", lst)
        else:
            print("Loop ", loop)
            print(sort_list + unsort_list)
            sort_list.append(lst[ind])
            unsort_list.pop(0)
            for sortlist_ind in range(-1, -len(sort_list), -1):
                cur = sort_list[sortlist_ind]
                nxt = sort_list[sortlist_ind-1]
                print(sort_list)
                if cur > nxt:
                    temp = sort_list[sortlist_ind]
                    sort_list[sortlist_ind] = sort_list[sortlist_ind-1]
                    sort_list[sortlist_ind-1] = temp
                else:
                    break

        loop += 1
    print("Final Sorted List: ", sort_list)
    return sort_list


lst = []
orig_list=[]
count = 1
while count <= 7:
    try:
        if count == 1:
            inp = int(input("Enter 7 numbers\n: "))
            while inp in lst:
                print("Item already exists! Type again.")
                inp = int(input(": "))
                
        else:
            inp = int(input(": "))
            while inp in lst:
                print("Item already exists! Type again.")
                inp = int(input(": "))
        lst.append(inp)
        orig_list.append(inp)
        count += 1
    except ValueError:
        print("Wrong Input!")

choice = 0
while choice != 4:
    print(40*"=")
    print("\t\tMenu ")
    print(40*"=")
    print("\t[1] Bubble Sort")
    print("\t[2] Selection Sort")
    print("\t[3] Insertion Sort")
    print("\t[4] Exit")
    print(40*"=")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Wrong Input!")
    lst = orig_list.copy()
    if choice == 1:
        choice2 = ""
        while choice2 != "a" and choice2 != "b" and choice2 != "c":
            print(40*"=")
            print("\t\tBubble Sort ")
            print(40*"=")
            print("\t[a] Ascending Order")
            print("\t[b] Descending Order")
            print("\t[c] Go Back to Menu")
            print(40*"=")
            choice2 = input("Enter your choice: ")
            choice2 = choice2.lower()
            if choice2 == "a":
                #lst = orig_list.copy()
                bubble_asc(lst)
            elif choice2 == "b":
                #lst = orig_list.copy()
                bubble_desc(lst)
            elif choice2 == "c":
                continue
            else:
                print("Wrong Input! Try Again.")

    elif choice == 2:
        choice2 = ""
        while choice2 != "a" and choice2 != "b" and choice2 != "c":
            print(40*"=")
            print("\t\tSelection Sort ")
            print(40*"=")
            print("\t[a] Ascending Order")
            print("\t[b] Descending Order")
            print("\t[c] Go Back to Menu")
            print(40*"=")
            choice2 = input("Enter your choice: ")
            choice2 = choice2.lower()
            if choice2 == "a":
                #lst = orig_list.copy()
                sel_asc(lst)
            elif choice2 == "b":
                #lst = orig_list.copy()
                sel_desc(lst)
            elif choice2 == "c":
                continue
            else:
                print("Wrong Input! Try Again.")

    elif choice == 3:
        choice2 = ""
        while choice2 != "a" and choice2 != "b" and choice2 != "c":
            print(40*"=")
            print("\t\tInsertion Sort ")
            print(40*"=")
            print("\t[a] Ascending Order")
            print("\t[b] Descending Order")
            print("\t[c] Go Back to Menu")
            print(40*"=")
            choice2 = input("Enter your choice: ")
            choice2 = choice2.lower()
            if choice2 == "a":
                #lst = orig_list.copy()
                insert_asc(lst)
            elif choice2 == "b":
                #lst = orig_list.copy()
                insert_dec(lst)
            elif choice2 == "c":
                continue
            else:
                print("Wrong Input! Try Again.")

    elif choice == 4:
        print("Exitting Program.. ")


            
        
    





