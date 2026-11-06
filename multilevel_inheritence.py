class grandparent:
    def display(self):
        print("Grand parent")
class Parent(grandparent):
    def show(self):
        print("Parent")
        
class child(Parent):
    def show1(self):
        print("Child")
        
obj=child()
obj.display()
obj.show()
obj.show1()
