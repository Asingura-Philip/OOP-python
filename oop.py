# class variables
class Student:

    class_year = 2024
    num_students = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("gojo",30)
student2 = Student("geto",29)
student3 = Student("toji",24)

# print(Student.class_year)
# print(Student.num_students)

# inheritance

class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF")
class Cat(Animal):
    def speak(self):
        print("MEOW")
class Mouse(Animal):
    def speak(self):
        print("SQUEEK")

dog = Dog("bolt")
cat = Cat("tom")
mouse = Mouse("jerry")

# print(dog.name)
# cat.eat()
# mouse.sleep()

# multiple inheritance
class Predator:
    def hunt(self):
        print("this animal is hunting")

class Prey:
    def flee(self):
        print("this animal is fleeing")


class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Predator,Prey):
    pass

fish = Fish()
fish.hunt()
fish.flee()