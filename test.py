def add(a,b):
    return a + b

# print(add(3,5))


# calc
print('welcome to the calculator')
print('select options')
print('1.add\n 2.subtract\n 3.multiply \n 4.divide')
option = int(input())
if option == 1:
    print('enter first number')
    number1 = int(input())
    print('enter second number')
    number2 = int(input())
    sum = number1 + number2
    print(f"the sum is {sum}")

elif option == 2:
    print('enter first number')
    number1 = int(input())
    print('enter second number')
    number2 = int(input())
    difference = number1 - number2
    print(f"the difference is {difference}")

elif option == 3:
    print('enter first number')
    number1 = int(input())
    print('enter second number')
    number2 = int(input())
    product = number1 * number2
    print(f"the product is {product}")

elif option == 4:
    print('enter first number')
    number1 = int(input())
    print('enter second number')
    number2 = int(input())
    quotient = number1 / number2
    print(f"the quotient is {quotient}")
else:
    print('unknown request')

# using functions

print('enter num1')
num1 = int(input())
print('enter num2')
num2 = int(input())

def sum(a,b):
    return a + b

print(sum(num1,num2))