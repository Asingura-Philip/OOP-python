x = 4
# print(x)

name = "Jackson"
# print(name)


# print("Hello, what is your name?")
# fname = input("enter firstname: ")
# print("nice to meet you " + fname)
# print("how old are you")
# age = input("enter age: ")

# print(fname + " is " + age + " years old")
#  f strings
# print(f"you are not so old {fname}")

nums = [3, 5, 7]

# print(nums)

# if statements

# age = int(input("Enter age: "))

# if age < 0:
#     print("not a valid age")
# elif age > 0:
#     print("valid age")
# else:
#     print("age is 0")

# lists

grades = ['a', 'x', 'c', 'z', 'e']
grades.append('w')
# print(grades)
grades.sort()
# print(grades)

# sets
my_set = {1,4,5,6,7}
my_set.add(9)
my_set.remove(5)
# print(my_set)

# print(f"my set has {len(my_set)} values")

# loops

#list loops
"""
for i in [0,1,2,3,4]:
    print(i)


numbers = ['a','b','c','d','e']

for i in numbers:
    print(i)

"""

# dict loops
"""
my_dict = {
    'name':"jafferson",
    'age': 19,
    'occupation': "painter",
}

for key,value in my_dict.items():
    print(key,value)

"""

#functions
"""
def add(x,y):
    return x+y

# print(add(4,5))

def greet(name):
    print(f"Good morning {name}")

greet('polin')
"""

# classes

class Person():
    def __init__(self,name,age,occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

person1 = Person("lino",45,"farmer")

# print(person1.name)

def divide(x,y):
    return x/y

# print(divide(0,3))

# print(1//2)

# x = int(input())
# y = int(input())
 
# x = x // y
# y = y // x
 
# print(y)
    
x = 4
# print(x)
del x
# print(x)


# find the largest of three numbers entered by the user
num1 = input('enter first number: ')
num2 = input('enter second number: ')
num3 = input('enter third number: ')

if num1 > num2 and num1 > num3:
    print('first number is the biggest')
elif num2 > num1 and num2 > num3:
    print('second number is the biggest') 
elif num3 > num2 and num3 > num1:
    print('third number is the biggest')