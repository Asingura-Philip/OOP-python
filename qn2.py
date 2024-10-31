# qn2
# a
def add_student(student_list, student_id, name, age, course):
    for student in student_list:
        if student['id'] == student_id:
            print("Error: Student ID already exists!")
            return
    student_list.append({'id': student_id, 'name': name, 'age': age, 'course': course})
# b
def find_student_by_id(student_list, student_id):
    for student in student_list:
        if student['id'] == student_id:
            return student
    print("Error: Student not found!")
    return None

def remove_student_by_id(student_list, student_id):
    for student in student_list:
        if student['id'] == student_id:
            student_list.remove(student)
            return
    print("Error: Student not found!")
# c
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def study(self):
        print(f"Student is studying {self.course}.")

class Instructor(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"Instructor is teaching {self.subject}.")

# 
def demonstrate_polymorphism():
    student = Student("Getrude", 30, "Computer Science")
    instructor = Instructor("Bob", 45, "Engineering")

    print(student)  # Calls __str__ from Person
    student.study()  # Calls Student's method

    print(instructor)  # Calls __str__ from Person
    instructor.teach()  # Calls Instructor's method

demonstrate_polymorphism()
# d
def sort_students(student_list, key_function):
    return sorted(student_list, key=key_function)

# Example usage
students = [
    {'id': '1', 'name': 'Getrude', 'age': 30, 'course': 'Computer Science'},
    {'id': '2', 'name': 'Charlie', 'age': 22, 'course': 'Engineering'},
    {'id': '3', 'name': 'Bob', 'age': 19, 'course': 'Dentistry'},
]

# Sorting by age
sorted_by_age = sort_students(students, key=lambda x: x['age'])
print("Sorted by age:", sorted_by_age)

# Sorting by name
sorted_by_name = sort_students(students, key=lambda x: x['name'])
print("Sorted by name:", sorted_by_name)


# usage
# Initialize student list
students = []

# Add students
add_student(students, '1', 'Getrude', 30, 'Computer Science')
add_student(students, '2', 'Charlie', 22, 'Engineering')
add_student(students, '3', 'Bob', 19, 'Dentistry')

# Find a student
print(find_student_by_id(students, '2'))  # Should return Charlie's details

# Remove a student
remove_student_by_id(students, '1')  # Removes Getrude

# Check remaining students
print(students)

# Demonstrate polymorphism
demonstrate_polymorphism()

# Sort students
sorted_by_age = sort_students(students, key=lambda x: x['age'])
print("Sorted by age:", sorted_by_age)

sorted_by_name = sort_students(students, key=lambda x: x['name'])
print("Sorted by name:", sorted_by_name)
