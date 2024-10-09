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

print(Student.class_year)
print(Student.num_students)