#In Python polymorphism does not have method overloadind it means no means to save 
#function name with different perameter 

#Python Only have method over Writing


class dad:
    def house(self):
        print("Color Yellow")
    def factory(self):
        print("Color Blue")

class son(dad):
    def business(self):
        print("Color White")

    def house(self):
        print("Color white")


obj_1 =son()
obj_1.house()
