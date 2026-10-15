from abc import ABC,abstractmethod

class Animal(ABC):

    @abstractmethod
    def canbark(self):
        pass
    @abstractmethod
    def canwlak(self):
        pass

    def sit(self):
        pass

class Species(Animal):
    def canbark(self):
        print("Dog can bark")

    def canwlak(self):
        print("Dog can walk")

obj1 = Species()
obj1.canwlak()
obj1.canbark()

#we cannot create object for abstract class that mean parent class
