#SOFIA JOY D. YUNUN 
print("Name: Sofia Joy D. Yunun \n")
myListA = [2,5,8,1,4,7,3,6,9,1]
print("a. myListA: ", myListA)
#index     0 1 2 3 4 5 6 7 8 9
myListB = []
for x in range(0,10): #range(0(start),10(end))
    x = int(input("Enter a number: "))#user input the numbers
    myListB.append(x)#add all the users-input(x) in the myListB
print("b. myListB: ", myListB)
aList = myListA[0:5]#2,5,8,1,4
bList = myListB[-5:]#6,1,2,3,2
for item in bList:#items in bList will be added to aList 
    aList.append(item)
print("c. myListC (unsorted): ", aList)
myListC = sorted(aList) #cannot used sort() as it returns None
print("d. myListC (sorted): ", myListC)
myListD = []
myListE = []
for a in myListA: #a = items in myListA
    if (a % 2) != 0: #even
        myListD.append(a)
print("e. myListD: ", myListD)
for i in myListB: #i = items in myListB
    if (i % 2) == 0: #even
        myListE.append(i)
print("f. myListE: ", myListE)
dList = [1,2,3,4,5]
eList = [6,7,8,9,10]
myListD.extend(dList)
print("g. myListD (added): ", myListD)
myListE.extend(eList)
print("h. myListE (added): ", myListE)
print("j. Final List:")
print("myListA: ", myListA)
print("myListB: ", myListB)
print("myListC: ", myListC)
print("myListD: ", myListD)
print("myListE: ", myListE)

    
    
    
