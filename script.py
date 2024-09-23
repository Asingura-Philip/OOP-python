# def my_generator():
#     yield 1
#     yield 2
#     yield 3

# for value in my_generator():
#     print(value)

# def my_function(*args):
#     for arg in args:
#     print(arg)

# my_function(1,2,3)

x = 10
def my_function():
    global x
    x = 20
my_function()
print(x)