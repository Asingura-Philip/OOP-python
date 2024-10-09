# class variables
class Student:

    class_year = 2024
    num_students = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age

student1 = Student("gojo",30)
student2 = Student("geto",29)

print(student1.class_year)