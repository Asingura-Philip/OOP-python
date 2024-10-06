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
        new_milage = distance + self.mileage
        return new_milage
        


# car1 = Car("toyota","d3",2008,15000)
# car2 = Car("mercedes","yd3",2008,5230)
# car3 = Car("ford","CT3",2008,50000)

# car1.display_info()
# car2.display_info()
# car3.display_info()


car4 = Car("Bentley","e4",2019,50000)
print(car4.drive(100))
car4.display_info()