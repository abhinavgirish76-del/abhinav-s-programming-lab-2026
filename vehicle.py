class vehicle:
    def display1(self):
        print("4-6 Wheels")
        print("Blue in colour")
        print("Diesel Vehicle")
        print("190 kilo meter speed")
    def start(self):
        print("Start")
    def accelerate(self):
        print("Accelerate")
    def brake(self):
        print("Brake !!!!!!")
        
class car(vehicle):
    def display2(self):
        print("4 doors")
        
class Truck(vehicle):
    def display3(self):
        print("Size of containers")
    def loadContainer(self):
        print("Load Container")
        
        
class van(vehicle):
    def loadVan(self):
        print("No. Of Boxes ")
        
class bike(vehicle):
    def display4(self):
        print("Saddle Height")
        
class passengervehicle(vehicle):
    def display5(self):
        print("Passenger Seats ")

class transportation_vehicle(vehicle):
    def display6(self):
        print("No. of Doors")
        print("Load Capacity")
        
obj1=vehicle()
obj2=passengervehicle()
obj3=bike()
obj4=van()
obj5=Truck()
obj6=car()

obj8=transportation_vehicle()

obj1.display1()
obj6.display2()
obj5.display3()
obj5.loadContainer()
obj4.loadVan()
obj3.display4()
obj2.display5()
obj8.display6()