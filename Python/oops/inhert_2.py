from Python.oops.inhert_1 import father
class son(father):
    def factory(self):
        print("Factory color is Yellow")
    
    
obj2=son()
obj2.house()
obj2.factory()

