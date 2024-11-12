def Ascending(mergelist):
    print("Splitting", mergelist)
    if len(mergelist)>1:
        mid = len(mergelist)//2
        lefthalf = mergelist[:mid]
        righthalf = mergelist[mid:]

        Ascending(lefthalf)
        Ascending(righthalf)

        i=j=k=0
        while i< len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf [j]:
                mergelist[k] = lefthalf[i]
                i+=1
            else:
                mergelist[k] = righthalf[j]
                j+=1
            k+=1

        while i < len(lefthalf):
            mergelist[k] = lefthalf [i]
            i+=1
            k+=1

        while j < len(righthalf):
            mergelist[k] = righthalf [j]
            j+=1
            k+=1
    print("Merging" , mergelist)
def Descending(mergelist):
    print("Splitting", mergelist)
    if len(mergelist)>1:
        mid = len(mergelist)//2
        lefthalf = mergelist[:mid]
        righthalf = mergelist[mid:]

        Descending(lefthalf)
        Descending(righthalf)

        i=j=k=0
        while i< len(lefthalf) and j < len(righthalf):
            if lefthalf[i] > righthalf [j]:
                mergelist[k] = lefthalf[i]
                i+=1
            else:
                mergelist[k] = righthalf[j]
                j+=1
            k+=1

        while i < len(lefthalf):
            mergelist[k] = lefthalf [i]
            i+=1
            k+=1

        while j < len(righthalf):
            mergelist[k] = righthalf [j]
            j+=1
            k+=1
    print("Merging" , mergelist)
lst = []
orig_list = []
count = 1
while count <= 8:
    try:
        if count == 1:
            inp = int(input("Number "+str(count)+" :"))
            while inp in lst:
                print("Item already exists! Type again.")
                inp = int(input("Number "+str(count)+" :"))
                
        else:
            inp = int(input("Number "+str(count)+" :"))
            while inp in lst:
                print("Item already exists! Type again.")
                inp = int(input("Number "+str(count)+" :"))
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
    print("\t[1] Ascending")
    print("\t[2] Descending")
    print("\t[3] Exit")
    print(40*"=")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Wrong Input!")
    
    if choice == 1:
        Ascending(lst)
        print("Final List: ",lst)

    elif choice == 2:
       Descending(lst)
       print("Final List: ",lst)
       

    elif choice == 3:
         print("Exitting Program.. ")
       
