"""
Getting users numbers and adding
them togther and returning the result
"""
# Basic Calculator
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)
# int() in results or float(). int() used for whole numbers whereas float allows decimals
print(result)

# Better Calculator
number1 = float(input("Enter first number: "))
op = input("Enter operator: ")
number2 = float(input("Enter Second Number: "))

if op == '+':
    print(number1 + number2)
elif op == '-':
    print(number1 - number2)
elif op == '/':
    print(number1 / number2)
elif op == '*':
    print(number1 * number2)
else:
    print("Invalid operator")
