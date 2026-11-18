class Parent:
    def display1(self):
        print("This is parent class Feature")
class child1(Parent):
    def display2(self):
        print("This is child 1's Feature")
class child2(Parent):
    def display3(self):
        print("This is child 2's Feature")

obj1=child1()
obj2=child2()
obj1.display2()
obj2.display3()
obj3=Parent()
obj3.display1()