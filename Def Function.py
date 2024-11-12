user = input("Username: ")
print("✿"*40)
print("\n\t☆☆  Welcome ", user," to the Final Case Study of  ☆☆" )
print("\t\t☆ SOFIA JOY D. YUNUN from ICT - 106 ☆")
print("\n"+"✿"*40)
def main():
    menu()
        
def menu():
    print("\n\t\t\t◃┆ MAIN MENU ┆▷")
    print("\n\tChoose what Term you prefer. Please type the assigned \n\t\tletter for each in the section provided.")
    pre = print("\n\t\t\t◃ [P] Prelim ▷")
    mid = print("\n\t\t\t◃ [M] Midterm ▷")
    fin = print("\n\t\t\t◃ [F] Finals ▷")
    user1 = input("\n▷▷▷ Enter your answer here: ")
    user1a = user1.lower()
    if user1a == "p":
        prelim()
        again()
    elif user1a == "m":
        midterm()
        again()
    elif user1a == "f":
        finals()
        again()
    elif user1a != "p" or "m" or "f":
        print("Please type the required LETTER. Thank you (◠ω◠✿)")
        
def again():
    print("\n\tDo you want to continue?( ́ ◕◞ε◟◕`)")
    pre = print("\n\t\t◃ [Y] Yes ▷")
    mid = print("\n\t\t◃ [N] No ▷")
    user1 = input("\n▷▷▷ Enter your answer here: ")
    user1a = user1.lower()
    for a in user1a:
        if a == "y":
            print("✿"*40)
            menu()
        else:
            print("✿"*40)
            thank()

def prelim():
    print("✿"*40)
    pweek2()
    print("✿"*40)
    pweek4()
    print("✿"*40)
    plab1()
    print("✿"*40)
    print()
    
def midterm():
    print("✿"*40)
    mweek5()
    print("✿"*40)
    mweek8()
    print("✿"*40)
    mweek9()
    print("✿"*40)
    mweek11()
    print("✿"*40)
    print()
    
def finals():
    print("✿"*40)
    fweek14()
    print("✿"*40)
    fweek16()
    print("✿"*40)
    print()

def pweek2():
    print("\n\t☆ Prelim Week 2 ☆\n#Number 1")
    print ("Welcome to Python Programming Course!\nThis is a simple program in\n\tPython!")
    print()
    print("#Number 2")
    a = input ("Enter a character: ")
    b = input ("Enter the first word: ")
    c = input ("Enter the second word: ")
    d = input ("Enter the third word: ")
    e = input ("Enter the fourth word: ")
    f = input ("Enter the fifth word: ")
    print (b+" "+a+" "+c+" "+a+" "+d+" "+a+" "+e+" "+a+" "+f)
    print()
    print("Number 3")
    x = int(input("Input the value for x: "))
    y = int(input("Input the value for y: "))
    z = int(input("Input the value for z: "))
    a = (3*(x*x*x)*(y*y)*(z*z*z)+x)/(x+y+z)
    print(round(a,2))

def pweek4():
    print("\n\t☆ Prelim Week 4 ☆")
    name = input("Please enter your name: ")
    print (name + " , do you want to know your cost in electricity meter in Kilowatt per hour?")
    answer = int(input("If yes press 1 and 2 if not. \nHere:"))
    if answer == 1:
        power = int(input("Enter your electricity meter reading: "))
        if power >= 0 and power <=100:
            a = 150.00
            print ("The cost is: " + str(a))
        elif power >= 101 and power <= 500:
            a = 150.00
            b = 0.5
            c = a + b
            print ("The cost is: " + str(c))
        elif power >= 501:
            a = 350.00
            b = 0.3
            c = a + b
            print ("The balance is: " + str(c))
    elif answer == 2:
        print("Okay, thank you for visiting.")

def plab1():
    print("\n\t☆ Prelim Exam Laboratory ☆")
    print("*"*50)
    print("\t\tMJ Lawn-Mowing Services")
    print("*"*50)
    w=int(input("Enter the width of the lot(ft): "))
    l=int(input("Enter the length of the lot(ft): "))
    ans=w*l
    print()
    if ans<4000:
        a=50000
        b=2
        fir=a*b
        print("The total lot in square feet (sq.ft): " + str(ans))
        print("Weekly mowing fee is: $ "+str(a))
        print("Number of lawn-mowing weeks of the lot (season): "+str(b))
        print("Total season lawn-mowing fee: $ "+ str(fir))
    print()
    if ans>4000 and ans<6000:
        a=75000
        b=5
        sec=a*b
        print("The total lot in square feet (sq.ft): " + str(ans))
        print("Weekly mowing fee is: $ "+str(a))
        print("Number of lawn-mowing weeks of the lot (season): "+str(b))
        print("Total season lawn-mowing fee: $ "+ str(sec))
    print()
    if ans>=6000:
        a=100000
        b=6
        thi=a*b
        print("The total lot in square feet (sq.ft): " + str(ans))
        print("Weekly mowing fee is: $ "+str(a))
        print("Number of lawn-mowing weeks of the lot (season): "+str(b))
        print("Total season lawn-mowing fee: $ "+ str(thi))
    print()
    print("Choose Payment Plan: [1]Full [2]Installment")
    ans1=input("Enter your choice: ")
    if ans1==2:
        a=input("Enter number of installment: ")
        print("Number of payment: "+ str(a))
        if ans<4000:
            div=fir/a
            if a==2:
                total=div+0.05
                last=fir+total
                print("Service change per due: $ "+ str(div))
                print("Total pay per due: $ "+ str(total))
                print("Total payment for the season: $ "+ str(last))
            elif a>=3:
                total1=div+0.1
                last1=fir+total
                print("Service change per due: $ "+ str(div))
                print("Total pay per due: $ "+ str(total1))
                print("Total payment for the season: $ "+ str(last1))
        if ans>4000 and ans<6000:
            div=sec/a
            if a==2:
                total=div+0.05
                last=sec+total
                print("Service change per due: $ "+ str(div))
                print("Total pay per due: $ "+ str(total))
                print("Total payment for the season: $ "+ str(last))
            elif a>=3:
                total1=div+0.1
                last1=sec+total
                print("Service change per due: $ "+ str(div))
                print("Total pay per due: $ "+ str(total1))
                print("Total payment for the season: $ "+ str(last1))
        if ans>=6000:
            div=thi/a
            if a==2:
                total=div+0.05
                last=thi+total
                print("Service change per due: $ "+ str(div))
                print("Total pay per due: $ "+ str(total))
                print("Total payment for the season: $ "+ str(last))
            elif a>=3:
                total1=div+0.1
                last1=thi+total
                print("Service change per due: $ "+ str(div))
                print("Total pay per due: $ "+ str(total1))
                print("Total payment for the season: $ "+ str(last1))
    elif a==1:  
        print("Number of payment: Full")
        if ans<4000:
            print("Service change per due: $ "+ str(fir))
            print("Total pay per due: $ "+ str(fir))
            print("Total payment for the season: $ "+ str(fir))
        elif ans>4000 and ans<6000:
            print("Service change per due: $ "+ str(sec))
            print("Total pay per due: $ "+ str(sec))
            print("Total payment for the season: $ "+ str(sec))
        elif ans>=6000:
            print("Service change per due: $ "+ str(thi))
            print("Total pay per due: $ "+ str(thi))
            print("Total payment for the season: $ "+ str(thi)) 

def mweek5():
    print("\n\t☆ Midterm Week 5 ☆")
    try:
        print("Hello, Want to use Mathematical Equations?")
        print("Please enter the two number first below.")
        print("Press 1 if addition, 2 if subtraction, 3 if multiplication and 4 for division.")
        ans=int(input("Enter your answer here: "))
        print("The two numbers, below:")
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        if ans == 1:
            add=a+b
        elif ans == 2:
            sub=a-b
        elif ans == 3:
            mul=a*b
        elif ans == 4:
            div=a/b
    except NameError as err:
        print("There is a name error", err)
        add = ("No answer")
        sub = ("No answer")
        mul = ("No answer")
        div = ("No answer")
        ans = 0
    except ValueError as err:
        print("There is a value error", err)
        add = ("No answer")
        sub = ("No answer")
        mul = ("No answer")
        div = ("No answer")
        ans = 0
    except ZeroDivisionError:
        print("Cannot be divided to 0")
        add = ("No answer")
        sub = ("No answer")
        mul = ("No answer")
        div = ("No answer")
        ans = 0
    else:
        print("No Error")
    finally:
        if ans == 1:
            print(add)
        elif ans == 2:
            print(sub)
        elif ans == 3:
            print(mul)
        elif ans == 4:
            print(div)
        print("Thank you for using.")
        
def mweek8():
    print("\n\t ☆ Midterm Week 8 ☆")
    try:
        name=input("Enter your name to continue: ")
        print("Hello, " + name + ", Welcome to Even and Odd Counter!")
        num=int(input("Enter a digit sequence: "))
        num1 = num
        n=0
        while num != 0: 
            num = num // 10 #using float divide in order for the loop to meet an end which is 0
            n += 1          #that is why num is not equal to 0 for the loop to still continue
        print("Digit sequence count: "+ str(n))
        a=[] # serve as an empty space used for storing data later
        a_eve=[] # serve as an empty space used for storing data later
        a_odd=[] # serve as an empty space used for storing data later
        eve = 0 # need for looping in counter
        odd = 0 # need for looping in counter
        for i in range(1,n+1): #need n+1 because end point do not include the last number
            a.append(i) # this section adds the existing list
        # for instance we print(a) the result would be [the user's numbers with comma]
        for i in a:
            if i % 2 == 0: #divisible by 2 = even and equals to zero since remainder is being used
                a_eve.append(i)
                eve+=1 
            else: # and afcourse contrast of being divisible by 2 is odd
                a_odd.append(i)
                odd+=1
        print(eve, " even numbers:")
        print(a_eve)
        print(odd, " odd numbers:")
        print(a_odd)
    except:
        print("Your input contains letters.Please make it numerical Only.")

def mweek9():
    print("\n\t☆ Midterm Week 9 ☆")
    name = input("Please enter your name: ")
    print ("Hello " + name + ", Welcome to Palindrome Game!")
    ans = int(input("Enter 1 to continue, and 2 if not: \n"))
    if ans == 1: 
        a= input("Enter a word: ")
        a= a.lower()
        if a.isalpha() == True:
            b= a[::1]
            c= a[::-1]
            if b == c:
                print("PALINDROME (°∀°)")
            else:
                print("NOT PALINDROME <('o'<)")
        else:
            print("⊙﹏⊙ Sorry Invalid Input.\nPlease enter letters only.Thank you")
    elif ans == 2:
        print("Thank you for trying. (づ｡◕‿‿◕｡)づ")

def mweek11():
    print("\n\t☆ Midterm Week 11 ☆")
    def main():
        try:
            print("Welcome to Perimeter and Circumference Calculator!")
            print("Please press the number of your chosen shape:")
            print("[1]Circle\n[2]Triangle\n[3]Square\n[4]Rectangle\n[5]Parallogram")
            ans=int(input("Please enter your choice here: "))

            if ans == 1:
                sol_cir()
            elif ans == 2:
                sol_tri()
            elif ans == 3:
                sol_sq()
            elif ans == 4:
                sol_rec()
            elif ans == 5:
                sol_par()
        except NameError:
            print("!INVALID!\nPlease only choose from 1,2,3,4,5 keys. Thank you")
        except SyntaxError:
            print("!INVALID!\nPlease only choose from 1,2,3,4,5 keys. Thank you")
        

        def sol_cir():
            r=int(input("Enter the radius of the circle (m): "))
            ans1=2*3.1416*r
            print("The circumference is " + str(ans1) + " m")
        
        def sol_tri():
            a=int(input("Enter the length of the first side (m): "))
            b=int(input("Enter the length of the second side (m): "))
            c=int(input("Enter the length of the third side (m): "))
            ans1=a+b+c
            print("The perimeter is " + str(ans1)+ " m")

        def sol_sq():
            a=int(input("Enter the length of the square (m): "))
            ans1= 4*a
            print("The perimeter is " + str(ans1)+ " m")
    
        def sol_rec():
            a=int(input("Enter the length of the rectangle (m): "))
            b=int(input("Enter the width of the rectangle (m): "))
            ans1= 2* (a+b)
            print("The perimeter is " + str(ans1)+ " m")

        def sol_par():
            a=int(input("Enter the base of the parallelogram (m): "))
            b=int(input("Enter the side of the parallelogram (m): "))
            ans1= 2* (a+b)
            print("The perimeter is " + str(ans1)+ " m")
    main()  

def fweek14():
    print("\n\t☆ Finals Week 14 ☆")
    print("Welcome to Name Listing")
    a = input("Enter a name: ")
    b = input("Enter a name: ")
    c = input("Enter a name: ")
    d = input("Enter a name: ")
    e = input("Enter a name: ")
    f = input("Enter a name: ")
    g = input("Enter a name: ")
    h = input("Enter a name: ")
    i = input("Enter a name: ")
    j = input("Enter a name: ")
    lista = [a,b,c,d,e,f,g,h,i,j]
    if a.isalpha()and b.isalpha()and c.isalpha()and d.isalpha() and e.isalpha() and f.isalpha() and g.isalpha() and h.isalpha() and i.isalpha() and j.isalpha():
        print("\nThe name list: ",lista,"\n")
        a1 = len(a)
        a2 = len(b)
        a3 = len(c)
        a4 = len(d)
        a5 = len(e)
        a6 = len(f)
        a7 = len(g)
        a8 = len(h)
        a9 = len(i)
        a10 = len(j)
        odd = []
        eve = []
        if a1 % 2 == 0:
            eve.insert(0,a)
        else:
            odd.insert(0,a)
        if a2 % 2 == 0:
            eve.insert(0,b)
        else:
            odd.insert(0,b)
        if a3 % 2 == 0:
            eve.insert(0,c)
        else:
            odd.insert(0,c)
        if a4 % 2 == 0:
            eve.insert(0,d)
        else:
            odd.insert(0,d)
        if a5 % 2 == 0:
            eve.insert(0,e)
        else:
            odd.insert(0,e)
        if a6 % 2 == 0:
            eve.insert(0,f)
        else:
            odd.insert(0,f)
        if a7 % 2 == 0:
            eve.insert(0,g)
        else:
            odd.insert(0,g)
        if a8 % 2 == 0:
            eve.insert(0,h)
        else:
            odd.insert(0,h)
        if a9 % 2 == 0:
            eve.insert(0,i)
        else:
            odd.insert(0,i)
        if a10 % 2 == 0:
            eve.insert(0,j)
        else:
            odd.insert(0,j)
        #eve[] is where the stored even length names, nakastore lang sila since di sila nakaprint
        odd.sort(key = str.lower)
        print ("Odd length names (sorted alphabetically): ", odd)
    else:
        print("Please Enter Name Only. Thank you <3")

        #PS. Mam nagulo ako sa looping kaya tinry ko sa if else method :'>

def fweek16():
    print("\n\t☆ Finals Week 16 ☆")
    print("Welcome to Recording Station. Please Input the required details Below:")
    try:
        set1={
            "Name":input("Enter your Full name: "),
            "Address":input("Enter your Address: "),
            "Age":int(input("Enter your Age: ")),
            "Position":input("Enter the Position: ")
            }
        set2={
            "Name":input("Enter your Full name: "),
            "Address":input("Enter your Address: "),
            "Age": int(input("Enter your Age: ")),
            "Position":input("Enter the Position: ")
            }
        set3={
            "Name":input("Enter your Full name: "),
            "Address":input("Enter your Address: "),
            "Age": int(input("Enter your Age: ")),
            "Position":input("Enter the Position: ")
            }
        set4={
            "Name":input("Enter your Full name: "),
            "Address":input("Enter your Address: "),
            "Age": int(input("Enter your Age: ")),
            "Position":input("Enter the Position: ")
            }
        set5={
            "Name":input("Enter your Full name: "),
            "Address":input("Enter your Address: "),
            "Age": int(input("Enter your Age: ")),
            "Position":input("Enter the Position: ")
            }
        
        print("All Employee Records:")
        print("("+ "1 , ", set1 , ")")
        print("("+ "2 , ", set2 , ")")
        print("("+ "3 , ", set3 , ")")
        print("("+ "4 , ", set4 , ")")
        print("("+ "5 , ", set5 , ")")
        print("Angeles City Residents")
        a = set1.get("Address")
        a1 = a.lower()
        if a1 == "angeles city":
            print(1 ,set1)
        b = set2.get("Address")
        b1 = b.lower()
        if b1 == "angeles city":
            print(2 , set2)
        c = set3.get("Address")
        c1 = c.lower()
        if c1 == "angeles city":
            print(3 , set3)
        d = set4.get("Address")
        d1 = d.lower()
        if d1 == "angeles city":
            print(4 , set4)
        e = set5.get("Address")
        e1 = e.lower()
        if e1 == "angeles city":
            print(5 ,set5)
    except:
        print("Please input the RIGHT INFORMATION")

def thank():
    print("\n\tThank you for Visiting. ╰(◡‿◡✿╰)\n\tSee you next timeヾ(●⌒∇⌒●)ﾉ")
main()
    
