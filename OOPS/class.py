class student:
    rno=1
    name='Abhinav'
    branch='cse'
    def read(self):
        print("welcome to my class")
        rno=550
        print("Roll no. is ",self.rno)
        print("Instance variable ",self.rno)
obj=student()
print("Roll Number is",obj.rno)
print("Name is",obj.name)
print("Branch is",obj.branch)
obj.read()