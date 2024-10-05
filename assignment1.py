# Creating a Class and Objects
class Car:
    def __init__(self,brand,model,year,mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
    def display_info(self):
        print(f"this is a {self.year} {self.brand} {self.model} with a mileage of {self.mileage}")


car1 = Car("toyota","d3",2008,15000)
car2 = Car("mercedes","yd3",2008,5230)
car3 = Car("ford","CT3",2008,50000)