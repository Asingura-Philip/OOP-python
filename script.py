# # def my_generator():
# #     yield 1
# #     yield 2
# #     yield 3

# # for value in my_generator():
# #     print(value)

# # def my_function(*args):
# #     for arg in args:
# #     print(arg)

# # my_function(1,2,3)

# x = 10
# def my_function():
#     global x
#     x = 20
# my_function()
# # print(x)

# # lambda

# add = lambda x, y: x + y
# # print(add(2, 3))  # Output: 5


# numbers = [1, 2, 3, 4, 5, 6]
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# # print(evens)  # Output: [2, 4, 6]

# tuples = [(1, 'one'), (2, 'two'), (3, 'three')]
# sorted_tuples = sorted(tuples, key=lambda x: x[1])
# # print(sorted_tuples)  # Output: [(1, 'one'), (3, 'three'), (2, 'two')]


# class Dog:
#     def __init__(self,age, breed):
#         self.age = age
#         self.breed = breed
    
# dog1 = Dog(14,"lab")

# # print(dog1.age)

# gy = 9
# print(f"{gy:05d}")


# class to roll dice

# import random

# class Dice:
#     def __init__(self,num):
#         self.num = num
#     def roll():
#         randomNum = random.randint(1,6)
#         return randomNum


# decorators



def icing(func):
    def wrapper():
        print("icing on cake")
        func()
    return wrapper()

@icing
def bake():
    print("bake cake")


bake()