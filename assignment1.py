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
def create_car(brand, model, year, mileage):
    return {"brand": brand, "model": model, "year": year, "mileage": mileage}

def display_info(car):
    print(f"{car['year']} {car['brand']} {car['model']}, Mileage: {car['mileage']} miles")

def drive(car, distance):
    car['mileage'] += distance

# What differences did you notice between the OOP and procedural implementations?
# The OOP implemantation allows for code reusablility with inheretance while the procedural appraoch doesnt allow for that 

# How does OOP provide benefits like modularity, reusability, and maintainability compared to procedural programming?
# Modularity allows for the same code a task to be broken down into small parts
# reusablity is seen through inheritance 
# maintainability is an advantage because the code can be modified and added to without affecting its functionality