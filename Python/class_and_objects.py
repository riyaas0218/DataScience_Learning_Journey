class Student:
    def say_hello(self):
        print("Hello")

s1=Student()
s1.say_hello() #s1.say_hello(s1 ---> this called self back python run like this)



#Constructor

class Employee:
    def __init__(self,name,emp_id):
         self.name_x=name    #store Once
         self.emp_id_y=emp_id   #store Once
    def display(self):
        print(f"employee name is {self.name_x}")  #its store in constrc so we use how many time we want
         

    def id_dispaly(self):
        print(f"employee id is {self.emp_id_y}")

obj1 = Employee("Riyas",101)
obj1.display()
obj1.id_dispaly()