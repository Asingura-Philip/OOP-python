class Vehicle:
    def __init__(self,model,traveled,mileage):
        self.model = model
        self.traveled = traveled
        self.mileage = mileage
        self.__remaining_distance = self.mileage - self.traveled 

car = Vehicle("benz",80,5000)
# print(car.traveled)
car.__remaining_distance = 50
print(car.__remaining_distance)

    
