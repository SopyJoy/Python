#SOFIA JOY D. YUNUN CS-202
print("Name: Sofia Joy D. Yunun\n")
import random
gen = random.sample(range(10,30),15) #start=10, end=30, length = 15
print(gen)
les_20=[]
great_20=[]
for x in gen:
    if x < 20:
        les_20.append(x)

a = 0
for x in gen:
    if x > 20:
        great_20.append(x)
        a+=1

first4 = gen[:4]
last4 = gen[11:]
comb = first4 + last4
combsort = sorted(comb)

Yunun_File2 = open(r"C:\Users\Brgy. Sindalan\Downloads\Yunun_File2.txt","w+")
Yunun_File2.write("Name: Sofia Joy D. Yunun\n")
Yunun_File2.write("\nDisplay the numbers less than 20:\n" + str(les_20))
Yunun_File2.write("\nCount the numbers greater than 20:\n" + str(a))
Yunun_File2.write("\nCombine the first and last four numbers:\n" + str(comb))
Yunun_File2.write("\nSorted the numbers:\n" + str(combsort))

Yunun_File2.close()




