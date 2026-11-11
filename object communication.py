class A:
    def __init__(self,a):
        self.a=a
        
    def __lt__(self,other):
        if(self.a>other.a):
            return True
        else:
            return False

obj1=A(1)
obj2=A(2)
if(obj1>obj2):
    print(obj1, "is greater")
   
else:
    print(obj2,"OBJ2 is greater")