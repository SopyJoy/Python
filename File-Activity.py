File = open(r"C:\Users\Brgy. Sindalan\Downloads\info.txt", "r")
print("Name: " + File.readline())
a = 0
for x in range(4):
    FileLine = int(File.readline())
    a += FileLine
#average
ave = a / 4
#Print output
print("Student's Average: ", str(ave) + "\n")
if ave < 75:
    print("Final Remarks: Failed")
else:
    print("Final Remarks: Passed")
File.close()
