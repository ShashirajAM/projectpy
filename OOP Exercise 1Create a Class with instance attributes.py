#OOP Exercise 1: Create a Class with instance attributes

class vehicle:
    def __init__(self,max_speed,milage):
        self.max_speed=max_speed
        self.milage=milage
Bike=vehicle(140,20)
print(Bike.max_speed,Bike.milage)


    