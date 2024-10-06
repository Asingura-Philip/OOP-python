# Creating a Class and Objects
class Car:
    def __init__(self,brand,model,year,mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
    def display_info(self):
        print(f"this is a {self.year} {self.brand} {self.model} with a mileage of {self.mileage}")

    def drive(self,distance):
        self.mileage = distance + self.mileage
        return self.mileage
        


# car1 = Car("toyota","d3",2008,15000)
# car2 = Car("mercedes","yd3",2008,5230)
# car3 = Car("ford","CT3",2008,50000)

# car1.display_info()
# car2.display_info()
# car3.display_info()


car4 = Car("Bentley","e4",2019,50000)
print(car4.drive(100))
car4.display_info()


# QN 3
class ElectricCar(Car):
    def __init__(self,battery_capacity,charge_level):
        self.battery_capacity = battery_capacity
        self.charge_level = charge_level
    
    def charge(self,amount):
        return amount + self.charge_level
    
# 3c
# c. Write a brief explanation (4-5 sentences) on how the ElectricCar class demonstrates the principles of modularity, reusability, and maintainability.
# The use of the ElectricCar class allows for us to be able to us
# the Car class as a blueprint to create other classes through inheritance
# This allows us not to repeat ourselves by rewriting the attributes that are already shared
# This also ensures less code is written and that the code that is written can be reused


# Qn 4- Rewite using procedural programming
