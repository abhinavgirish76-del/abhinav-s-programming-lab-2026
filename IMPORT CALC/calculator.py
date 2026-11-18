# from calmodule import
import calmodule
while True:
    print("select the option")
    print("1.addition")
    print("2.substrct")
    print("3.multiply")
    print("4.division")
    print("5.exit")
    choice=int(input("enter your choice:"))
    a= int(input("enter the first no:"))
    b=int(input("enter the second no:"))
    if choice==1:
        print(a,"+",b,"=",calmodule.addition(a,b))
    elif choice==2:
         print(a,"-",b,"=",calmodule.substraction(a,b))
    elif choice==3:
        print(a,"*",b,"=",calmodule.multiplication(a,b))
    elif choice==4:
        print(a,"/",b,"=",calmodule.division(a,b))
    elif choice==5:
          print("program terminated")
          break
    else:
        print("invalid choice")