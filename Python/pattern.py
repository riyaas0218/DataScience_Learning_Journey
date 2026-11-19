
#half Diamond
for i in range(1,6):
    print()
    for j in range(1,i+1):
        print(" * ",end=" ")

for i in range(1,6):
    print()
    for j in range(6,i,-1):
         print(" * ",end=" ")


print("\n")
#Square Matrix
for i in range(1,11):
    for j in range(i,i+1):
        print( i ," X ",j," = ",i*j)

#Matrix Table
for i in range(1,11): 
    print(i,"Matrix Table")              
    for j in range(1,11):          
        print( j ," X ",i," = ",i*j)


#Check Palindrom without inbuild fucntions

a=input("Enter a String")
c=[]
b=[]
for i in range(len(a)):
    c.append(a[i])     

for i in range(len(a)-1,-1,-1):
    b.append(a[i])
ans="Palindrome"            
for i in range(len(a)):     
    if(c[i]!=b[i]):        
        ans="Not Palindrome"                                                    
print(ans)                  


    
                                    
                                    