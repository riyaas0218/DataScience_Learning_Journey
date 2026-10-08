a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter  a number"))

if(a>b and a>c):
    print("a is biggest")
elif(b>a and b>c):
    print("b is biggest ")
else:
    print("c is biggest")



userlist=[]
for i in range(0,5):
    userlist.append(int(input("Enter a number")))

for i in userlist:
    if (i%2==0):
        print("even",i)
    else:
        print("odd",i)


numbers = [5, 15, 8, 20, 25, 3]
count=0
for i in numbers:
    if(i>20):
        count+=1
   
print(count)


number_list=[]
for i in range(0,5):
    number_list.append(int(input("Enter the number")))

min_num=number_list[0]
for num in number_list:
    if(min_num>num):
        min_num=num

print(min_num)
    
