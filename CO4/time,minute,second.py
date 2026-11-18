#create a class Time wiith private attribute hour ,minute,and second overload'+' operator find sum of time
class Time:
    def __init__(self):
        self.__h=int(input("Enter the time in hour"))
        self.__m=int(input("Enter the time in minute"))
        self.__s=int(input("Enter the time in Seconds"))
    def __add__(tob1,tob2):
        hours=(tob1.__h+tob2.__h)
        print("Sum of hourse",hours)
        minutes=(tob1.__m+tob2.__m)
        print("Sum of Minutes",minutes)
        seconds=(tob1.__s+tob2.__s)
        print("Sum of Seconds",seconds)
        if hours>=24:
            hours=hours%24
        if minutes>=60:
            hours=hours+minutes//60
            minutes=minutes%60
        if seconds>=60:
            minutes=minutes+seconds//60
            seconds=seconds%60
        return hours,minutes,seconds
print("Enter the time of first object")
tob1=Time()
print("Enter the time of second object")
tob2=Time()
print("sum of two time is (Hour,Minute,second)",tob1+tob2)
        