"""question2 create a class rectangle with private attribute length and width overload <operator compare the area of 2 rectangle
"""
class Rectangle:
    def __init__(self):
        self.__l=int(input("Enter the length"))
        self.__b=int(input("Enter the Woidth"))
    def __lt__(ob1,ob2):
        area1=ob1.__l*ob1.__b
        area2=ob2.__l*ob2.__b
        print("Area of Rectangle 1 is ",area1)
        print("Area of Rectangle 2 is ",area2)
        return area1>area2
print("Enter the length and breadth of first object : ")
ob1=Rectangle()
print("Enter the length and breadth of Secondobject")
ob2=Rectangle()
if ob1>ob2:
    print("Rectangle 1 is greater than Rectangle2")
else:
    print("Rectangle 2 is greater than rectangle1")
                     