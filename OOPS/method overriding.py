#method over ride
class father:
    def transportation(self):
        print("Cycle")
class son:
    def transportation(self):
        print("bike")
        
obj=son()
obj.transportation()

    