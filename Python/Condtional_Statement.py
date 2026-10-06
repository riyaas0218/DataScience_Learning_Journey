a=int(input("Enter a number"))5
if(a>0):
    print("this is positve number")
else:
    print("Its nagative number")

first = int(input("Enter a number"))
second = int(input("Enter a number"))
third = int(input("Enter a number"))

if(first>second and first > third):
    print("first number is high")
elif(second > first and second > third):
    print("second number is highests")
elif(third > first and third > second):
    print("third number is highest number")
else:
    print("enter a correct number")
