class father:
    def display(self):
        print("This is father's function")
class Mother:
    def display1(self):
        print("This is Mother's function")
class child(father,Mother):
    def display2(self):
        print("This is Child's feature ")
    
obj=child()
obj.display2()
obj.display()
obj.display1()
