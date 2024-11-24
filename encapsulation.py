class Vehicle:
    def __init__(self,model,traveled,mileage):
        self.model = model
        self.traveled = traveled
        self.mileage = mileage
        self.__remaining_distance = self.mileage - self.traveled 

    def drive(self):
        print(f'the {self.model} vehicle is moving')

class Taxi(Vehicle):
    def __init__(self,model,traveled,speed,mileage):
        super().__init__(model,traveled,mileage)
        self.speed = speed

    def drive(self):
        super().drive()
    # def drive(self):
    #     print(f'the taxi moves at {self.speed} km per hr')


car = Vehicle("benz",80,5000)
taxi1 = Taxi("noah",300,500,4000)
car.drive()
taxi1.drive()

# # print(car.traveled)
# car.__remaining_distance = 50
# print(car.__remaining_distance)

    
