class Vehicle:
    def __init__(self, name):
        self.name=name
    

class Bus(Vehicle):
    def __init__(self, name, fare):
         super().__init__(name)
         self.fare=fare

New_bus=Bus("Volvo",500 )
print("Bus name:", New_bus.name,",", "Bus fare:", New_bus.fare)