"""
Multiple different apps(name in comments above code)
By: Cassandra King
Date:
Note:
"""

# # Testing the water
# print("Hello World")
#
# # drawing a shape with print statements
# print("   /|  ")
# print("  / |")
# print(" /  |")
# print("/___|")
#
# # # Varibles and Data Types
# character_name = 'John'
# character_age = '35'
# is_male = True
# print("There once was a man named " + character_name + ',')
# print("he was " + character_age + " years old.")
# character_name = 'Mike'
# print("He really liked the name " + character_name + ', ')
# print("but didn't like being " + character_age + ".")
#
# # Working with Strings
# phrase = "Giraffe Academy"
# print(phrase.replace("Giraffe", "Elephant"))
#
# # Working with Numbers
# from math import *
# my_num = -5
# print(pow(3, 2))
# # abs() is absolute number, pow() is powers
# # round(), floor() ceil(), sqrt()
#
# # Getting inputs from users
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print('Hello ' + name + '! You are ' + age)

# Try Except(error checking?)(2/1/20)
try:
    awnser = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")
