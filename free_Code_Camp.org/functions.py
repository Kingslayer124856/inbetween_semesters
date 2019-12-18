"""
Working with functions
by; Cassandra King
Date; 18/12/19
"""


# a function that says hello to the user
def say_hello(name, age):
    print("Hello " + name + ", you are " + str(age))


say_hello("Jim", 76)
say_hello("Mike", 35)


# Return Statements
# cubing numbers function
def cube(num):
    return num * num * num


result = cube(3)
print(result)

# Working with If statements and simple boolens
is_male = True
is_tall = False
if is_male and is_tall:
    print("You are a tall Male")
elif is_male and not is_tall:
    print("You are a short male")
elif not is_male and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a Male and tall")


# If statements and comparisons
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(300, 40, 5))
