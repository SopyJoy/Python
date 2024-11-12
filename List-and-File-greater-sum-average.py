TD = [[10,12,1,3,7,8],[7,9,4,15,10,12],[18,4,6,7,8,9],[22,4,8,7,9,8],[3,5,13,20,19,10],[18,7,8,15,10,9]]
#Sum of numbers greater than 20
greater20 = 0
for main in range(len(TD)):
    for inner in range(len(TD[main])):
        array1 = TD[main][inner]
        if array1  > 20:
            greater20 += array1
print(greater20)

#average of main 0 & 1
countmain0 = 0
countmain1=0
for main_0 in range(6):
    array1 = TD[0][main_0]
    countmain0 += array1
print(countmain0)
for main_1 in range(6):
    array1 = TD[1][main_1]
    countmain1 += array1
print(countmain1)
ave_main_0_1 = (countmain0 + countmain1)/12
print(ave_main_0_1)

#sum of all values
sum_main=0
for main in range(len(TD)):
    for inner in range(len(TD[main])):
        array1 = TD[main][inner]
        sum_main += array1
print(sum_main)

#count of all values less than 10
less20 = 0
for main in range(len(TD)):
    for inner in range(len(TD[main])):
        array1 = TD[main][inner]
        if array1  < 10:
            less20 +=1
print(less20)

#main 4 in ascending order 3 5 10 13 19 20
rev_main4 = TD[4]
print(sorted(rev_main4))

#average of inner 2 & 3
countinner2 = 0
countinner3= 0
for main_0 in range(6):
    array1 = TD[main_0][2]
    countinner2 += array1
print(countinner2)
for main_1 in range(6):
    array2 = TD[main_1][3]
    countinner3 += array2
print(countinner3)
ave_inner_2_3 = (countinner2 + countinner3)/12
sum_1 =countinner2 + countinner3
print(sum_1)
print(ave_inner_2_3)

#file
File = open(r"C:\Users\SOC-Lab\Desktop\Result.txt","w+")
File.write("Sum of all numbers >20: " + str(greater20)+ "\n")
File.write("Average of main 0 & 1: " + str(ave_main_0_1)+ "\n")
File.write("Sum of all values: " + str(sum_main)+ "\n")
File.write("Count of all numbers <10: " + str(less20)+ "\n")
File.write("Main 4 in ascending order: " + str(rev_main4)+ "\n")
File.write("Average of inner 2 & 3: " + str(ave_inner_2_3)+ "\n")
File.close()

    
