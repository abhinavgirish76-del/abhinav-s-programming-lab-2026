#Abstract class
from abc import ABC,abstractmethod
class Aclass(ABC):
    @abstractmethod
    def display(self):
        None
class Demo(Aclass):
    def display(self):
        print("Abstract Methods")
obj1=Demo()
obj1.display()
        