class Vehicle:
    def __init__(self,color):
        self.color = color

    def getColor():
        pass

    def toString(self):
        print(f"This vehicle is {self.color}")


class Car(Vehicle):
    def __init__(self,winterTires=False):
        self.winterTires = winterTires
    def toString(self):
        print(f"This vehicle is {self.color}\n has winter tires: {self.winterTires}")