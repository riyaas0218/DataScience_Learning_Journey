odd_count=0
even_count=0

for i in range(1,11):
    if(i%2==0):
        even_count+=1
        print("Even",i)
    else:
        odd_count+=1
        print("Odd",i)

print(even_count)
print(odd_count)


exp=int(input("Enter a Experiance"))
salary=int(input("Enter a Salary"))
if(exp>=7 and exp<=10):
    salary=salary+(salary*50/100)
elif(exp>=5 and exp<7):
    salary=salary+(salary*30/100)
elif(exp>=2 and exp< 5):
    salary=salary+(salary*10/100)
elif(exp<2):
    print("No Salary increment")
else:
    print("enter your correct exp ")

print(salary)

first=int(input("Enter a number"))
second=int(input("Enter a number"))
third=int(input("Enter a number"))

if(first>=second and first>=third):
    print("first is large Number")
    if(first == second):
        print("first and second equal")
        if(first == third):
            print("all numbers are same")
    elif(first == third):
        print("first and third equal")

elif(second>=first and second>=third):
    print("second is larger number")
    if(second == first):
        print("second and first equal")
        if(second == third):
            print("all are equal")
    elif(second == third):
        print("second and third are same")

elif(third >= first and third >= second):
    print("third is large number")
    if(third == first):
        print("third and first equal")
        if(third == second):
            print("all numbers are same")
    elif(third == second):
        print("third and second same")
else:
    print("please give positve number")
        



year=int(input("enter a Year"))

if(year%400==0) or (year%4==0 and year%100 !=0):
    print("Leap Year")
else:
    print("Not Leap Year")

for i in range(0,10,2):
    print(i)

for i in range(0,11,-1):
    print(i)

word="Helllo Python"
for i in word:
    print(i,end='')


