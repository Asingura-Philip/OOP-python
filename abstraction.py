from abc import ABC ,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side * self.side
    
class Rectangle(Shape):
    def __init__(self,lenght,width):
        self.lenght = lenght
        self.width = width

    def area(self):
        return self.lenght * self.width
    