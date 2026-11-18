class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
    def perimeter(self):
        p=2*(self.l+self.b)
        print("The perimeter is",p)
    def compare(self,obj2):
        try:
            if obj1.area()==obj2.area():
                printf("Both are equal")
            elif obj1.area()>obj2.area():
                printf("area of rectangle 1 is greater than rectangle 2")
            elif obj1.area()<obj2.area():
                 printf("area of rectangle 2 is greater than rectangle 1")
        except:
           print("cant be compare")
l1=int(input("Enter the length of first rectangle"))
l2=int(input("Enter the length of second rectangle"))
b1=int(input("Enter the breadth of first rectangle"))
b2=int(input("Enter the breadth ofsecons rectangle"))
obj1=Rectangle(l1,b1)
obj2=Rectangle(l2,b2)
print("area of rectangle1",obj1.area())
print("area of rectangle2",obj2.area())
obj1.compare(obj2)
           
            
        