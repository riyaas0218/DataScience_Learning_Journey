class Parent:
    def __init__(self):
        self.public_var='I am Public'
        self._producted_var='I am Producted'
        self.__private_var='I am Private'

    def access_from_main(self):
        print("access from same class")
        print(self.public_var)
        print(self._producted_var)
        print(self.__private_var)

class Son(Parent):
    def access_from_subclass(self):
        print("Inside Chilred class")
        print(self.public_var)
        print(self._producted_var)
        try:
            print("Private",self.__private_var)
            #print("private",self._Parent__private_var)
            #this call NAME MANDLING that meanns we can use private var
            #without try except even though it is in strange class
            #here we say this is python philosophy ,if you know its private why you use NAME MAnDLING
            
        except AttributeError:
            print("Private Cannot be access by sub class")

class Stranger:
    def access_from_stragerclass(self,obj):
        print("Inside Stranger Class")
        print(self.public_var)
        print(self._producted_var)   #Not Recommented
        try:                                              
            print("Private",self.__private_var)           
        except AttributeError:                              
            print("Private Cannot be access by sub class")  


a=Parent()
b=Son()
c=Stranger()

a.access_from_main()
b.access_from_subclass()
c.access_from_stragerclass(a)
    


myList = []

for i in range(5):
    myList.append(int(input("Enter a Number: ")))

firstmax = max(myList)
secondmax = None

for i in myList:
    if i < firstmax:
        if secondmax is None or i > secondmax:
            secondmax = i

if secondmax is None:
    print("No second-largest distinct number")
else:
    print(secondmax)





myList = []

for i in range(5):
    myList.append(int(input("Enter a Number: ")))

for i in range(len(myList)):
    for j in range(len(myList)):
        if myList[i] < myList[j]:
            myList[i], myList[j] = myList[j], myList[i]

secondmax = myList[1]
print("Second largest:", secondmax)







