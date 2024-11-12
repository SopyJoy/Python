#File1
print("For File_1 info:")
name = input("Enter a name: ")
a = 0
b = 0
for x in range(3):
    quiz = int(input("Enter a Quiz score: "))
    a += quiz
ave1 = a/3
for y in range(2):
    assign = int(input("Enter an Assignment score: "))
    b += assign
ave2 = b/2
exam = int(input("Enter an Exam score: "))
file1={}
file1["Name: "]= name
file1["Quiz Average Score: "]= ave1
file1["Assignment Average Score: "]= ave2
file1["Exam Score: "]= exam

#File2
print("For File_2 info:")
name = input("Enter a name: ")
a = 0
b = 0
for x in range(3):
    quiz = int(input("Enter a Quiz score: "))
    a += quiz
ave1 = a/3
for y in range(2):
    assign = int(input("Enter an Assignment score: "))
    b += assign
ave2 = b/2
exam = int(input("Enter an Exam score: "))
file2={}
file2["Name: "]= name
file2["Quiz Average Score: "]= ave1
file2["Assignment Average Score: "]= ave2
file2["Exam Score: "]= exam


#File3
print("For File_3 info:")
name = input("Enter a name: ")
a = 0
b = 0
for x in range(3):
    quiz = int(input("Enter a Quiz score: "))
    a += quiz
ave1 = a/3
for y in range(2):
    assign = int(input("Enter an Assignment score: "))
    b += assign
ave2 = b/2
exam = int(input("Enter an Exam score: "))
file3={}
file3["Name: "]= name
file3["Quiz Average Score: "]= ave1
file3["Assignment Average Score: "]= ave2
file3["Exam Score: "]= exam

allFile = {
    "File1" : file1,
    "File2" : file2,
    "File3" : file3
    }
print(allFile)
#for record
Record = open(r"C:\Users\Brgy. Sindalan\Desktop\Record.txt", "w+")
Record.write("Name\t\tQuiz\t\tAssign\tExam")
for i in allFile:
    Record.write("\n")
    for c in allFile[i]:
        Record.write(str(allFile[i][c])+"\t\t")
Record.close()
