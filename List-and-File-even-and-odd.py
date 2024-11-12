TD=[[8,10,12,13,6],[7,8,12,7,9],[5,7,10,1,8],[3,5,5,3,5],[6,7,2,4,6]]
even = 0
odd = 0

for main in range(len(TD)):
    for inner in range(len(TD[main])):
        array1 = TD[main][inner]
        if array1 % 2 == 0:
            even+=1
        else:
            odd+=array1
            
print(even)
print(odd)

row_2 = 0
for row in range(len(TD[1])):
    array1 = TD[1][row]
    row_2 +=array1
print(row_2)

column_3 = 0
for column in range(len(TD[4])):
    array1 = TD[column][4]
    column_3 += array1
print(column_3)

diagonal_count = 0
for diagonal in range(5):
    array1 = TD[diagonal][diagonal]
    diagonal_count += array1
print(diagonal_count)

reverse_row3 = TD[2]
reverse_row3.reverse()
print(reverse_row3)

File = open(r"C:\Users\SOC-Lab\Desktop\W3_Lab1.txt","w+")
File.write("Even numbers: " + str(even)+ "\n")
File.write("Sum of Odd numbers: " + str(odd) + "\n")
File.write("Sum of Second Row: " + str(row_2)+ "\n")
File.write("Sum of Last column: " + str(column_3)+ "\n")
File.write("Sum of Vertical values: " + str(diagonal_count)+ "\n")
File.write("Reverse values of Row 3: " + str(reverse_row3)+ "\n")
File.close()

        
        
