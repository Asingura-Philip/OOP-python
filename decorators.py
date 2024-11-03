# Write a decorator called uppercase_decorator that converts the return value of a function to uppercase. Apply it to a function that returns a string.

def uppercase_decorator(func):
    def wrapper(*args,**kwargs):
        # func()
        value = func(*args,**kwargs)
        return value.upper()
    return wrapper

@uppercase_decorator
def get_name(name):
    
    # print(f"your name is {name}")
    return name


print(get_name("John"))