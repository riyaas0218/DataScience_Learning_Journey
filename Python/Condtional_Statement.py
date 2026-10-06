
a=int(input("Enter a number"))
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


age=18
has_licence="Yes"

if(age>=18):
    if(has_licence == "Yes"):
        print("You are Eligible to Drive")
    else:
        print("Get your Licence Soon")
else:
    print("Not Eligible")





correct_pin = '1234'
count = 0

while count < 3:

    enter_pin = input("Enter a PIN: ")

    if enter_pin == correct_pin:
        print("Access Granted")
        break

    count += 1
    print("Wrong PIN")

    if count == 3:
        print("Too Many Attempts. Access Blocked.")



#Pass  ---> it help to future logic implemetation that call palce holder ,we cannot write for loop without implemetaion so we use Pass


n=[10,-2,-5,2,6,2,-4,8,9,-1]

for num in n:
    if(num>0):
        print(num)
    continue