
# Your First Python Program
# print("Mosh Hamedani")


# How Code Gets Executed 
# print('o---')
# print(' |||| ')
# print('*' * 10)


# Variables 
# price = 10
# rating = 4.9
# name = 'Mosh'
# is_published = True
# print(price)


# Exercise : We check in a patient named John Smith. He's 20 years old and is a new partient.
# full_name = 'John Smith'
# age = 20 
# is_new = True
# print(full_name)
# print(age)
# print(is_new)



# Getting Input
# name = input('What is your name? ')
# print('Hi ' + name)

# Exercise : Ask two questions: person's name and favourite color. Then, print a message like "Mosh likes blue"

# name = input ('What is your name? ')
# color = input ('What is your favorite color? ')
# print(name + ' likes ' + color)


# Type Conversion
# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2023 - int(birth_year)
# print(type(age))
# print(age)


#  Ask a user their weight (in pounds), convert it to kilograms and print on the terminal.

#  weight_pounds = input('What is your weight in pounds? ')
#  print(type(weight_pounds))
#  weight_kilograms = float(weight_pounds) * 0.453592
#  print(weight_kilograms) 



# STRINGS

#  course = 'Python for Beginners'
#  print(course[0])
#  print(course[-2])
#  print(course[0:3])
#  print(course[0:])
#  print(course[1:])
#  print(course[:5])
#  another = course[:]
#  print(another)


#  name = 'Jennifer'
#  print(name[1:-1])
#  the result will be 'ennife'

# Formatted Strings
# first = 'John'
# last = 'Smith'
# message = first + ' [' + last + '] is a coder'
# msg = f'{first} [{last}] is a coder'
# print(msg)


# String methods
# course = 'Python for Beginners'
# print(course.upper())
# print(course.lower())
# print(course)
# print('python' in course)
# sum-up of String methods Tutorial: len() - counting characters, course.upper() - converting to UPPERCASE, course.lower() - converting to lowercase, course.title(), course.find() - returns the index, course.replace(), '...' in course


# Arithmetic Operations 
# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(10 ** 3)
# x = 10
# x = x + 3
# x += 3
# x -= 3
# print(x)


# Operator Precedence
# x = 10 + 3 * 2 ** 2 
# print(x)
# ranking in calculation of arithmetic operations
# parenthesis always take priority
# #1 exponentiation 2 ** 3
# #2 multiplication or division  
# #3 addition or substraction 
# EXERCISE
# x = (2 + 3) * 10 - 3
# print(x)


# Math Functions
# import math
# print(math.ceil(2.9)) the result will be 3
# print(math.floor(2.9)) the result here will be 2
# print(round(x)) the result will be 3
# print(abs(-2.9)) the result here will be 2.9


# If Statements

# is_hot = False
# is_cold = False

# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes") 
# else:
#     print("It's a lovely day") 
# print("Enjoy your day")

# EXERCISE: Price of a house is $1M. If buyer has good credit, they need to put down 10%, otherwise they need to put down 20%. Then, print the down payment
# price = 1000000
# has_good_credit = True

# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"Down payment: ${down_payment}")        


# Logical Operators
# if applicant has high income AND good credit score , then he is eligible for loan
# if applicant has good credit and doesnt have a criminal record then they eligible for loan
# and operator
# AND: both 
# OR: at least one
# has_high_income = False
# has_good_credit = False
# if has_high_income or has_good_credit:
#     print("Eligible for loan")

# has_good_credit = True
# has_criminal_record = True

# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan")




#Comparison Operators
# if temperature is greater than 30
# it's a hot day
#  otherwise if it's less than 10
#  it's a cold day
#  otherwise
#  it's neither hot nor cold


# temperature = 35

# if temperature > 30:
#      print("It's a hot day")
# else:
#      print("It's not a hot day")

# comparison operators : > , >= , <, <= , ==, != .

# Exercise : if name is less than 3 characters long, name must be at least 3 characters 
            # otherwise if it's more than 50 characters long name can be a maximum of 50 characters 
            # otherwise name looks good

# name = "marius"

# if len(name) < 3:
#     print("name must be at least 3 characters")
# elif len(name) > 50: 
#     print("name can be a maximum of 50 characters") 
# else:
#     print("name looks good!")     


#While loops 

# i = 1 
# while i <= 5:
    # print('*' * i)
    # i = i + 1 
# print("Done")    


# For Loops

# for item in 'Python':
    # print(item)

# for item in ['Mosh', 'John', 'Sarah']:
    # print(item)

# for item in [1, 2, 3 ,4]:
    # print(item)

# for item in range(10):
    # print(item)

# for item in range(5, 10):
    # print(item)    

# for item in range(5, 10, 2):
    # print(item)   

# Exercise: sum the prices in the array
# prices = [10, 20, 30]

# total = 0
# for price in prices:
    # total += price  #total = total + price
# print(f"Total: {total}")



# Nested loops 

# (x, y)
# (0, 0)
# (0, 1)
# (0, 2)
# (1, 0)
# (1, 1)
# (1, 2)


# for x in range(4):
    # for y in range(3):
        # print(f'({x},{y})')

# Exercise 
# terminal : F shape of x
# xxxxx
# xx
# xxxxx
# xx
# xx

# FIRST SOLUTION
# numbers = [5, 2, 5, 2, 2]

# for x_count in numbers:
    # print('x' * x_count)


# SECOND SOLUTION
# numbers = [5, 2, 5, 2, 2]

# for x_count in numbers: # in the first iteration x_count = 5; second = 2; third = 5; fourth = 2; fifth = 2.
    # output = '' # when x_count = 2 [index = 1], the output will be reseted again to an empty string.
    # for count in range(x_count): # x_count = 5 so range(x_count) would generate the numbers 0, 1, 2, 3, 4. The inner loop will be executed 5 times.
        # output += 'x'
    # print(output)



#  exercise 2 
# make in terminal a "L" shape made of "x"-es.

# numbers = [1, 1, 1, 1, 5]

# for x_count in numbers: 
    # output = '' 
    # for count in range(x_count): 
        # output += 'x'
    # print(output)




# Lists

# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# print(names) # ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# print(names[0])  # John
# print(names[2])  # Bob
# print(names[-1]) # last name: Mary 
# print(names[-2]) # last name after the last name: Sarah
# print(names[2:]) # ['Mosh', 'Sarah', 'Mary']
# print(names[2:4]) # ['Mosh', 'Sarah']
# print(names[0:]) # ['John', 'Bob', 'Mosh', 'Sarah', 'Mary'] 

# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# names[0] = 'Jon'
# print(names) # ['Jon', 'Bob', 'Mosh', 'Sarah', 'Mary']

# Write a program to find the largest number in a list

# numbers = [3, 6, 10, 2, 8, 4]
# max = numbers[0] # we just assume that the first item in the array is the largest number. We need to iterate through the array and compare it to max.
# for number in numbers:
    # if number > max:
        # max = number
# print(max)



# 2D Lists 

# [ 
    # 1 2 3
    # 4 5 6
    # 7 8 9 
# ]
# 3x3 

# matrix = [
    # [1, 2, 3],
    # [4, 5, 6],
    # [7, 8, 9]
# ]     
# matrix[0][1] = 20 
# print(matrix[0][1])
# for row in matrix:
    # for item in row:
        # print(item)




# List Methods
# numbers = [5, 2, 1, 7, 4]
# numbers.append(20) # [5, 2, 1, 7, 4, 20]
# print(numbers)
# numbers.insert(0, 10) # [10, 5, 2, 1, 7, 4]
# print(numbers)
# numbers.remove(5) # [2, 1, 7, 4]
# print(numbers)
# numbers.clear()
# print(numbers) # []
# numbers.pop() # removes the last item in a list: [5, 2, 1, 7]
# print(numbers)
# print(numbers.index(5)) # 0 because the index of 5 is 0
# print(numbers.index(50)) #ValueError: 50 is not in list
# numbers = [5, 2, 1, 7, 4]
# print(50 in numbers) # False
# numbers = [5, 2, 1, 5, 7, 4]
# print(numbers.count(5)) # 2
# print(numbers.sort()) # None - absence of value
# numbers = [5, 2, 1, 5, 7, 4]
# numbers.sort()
# print(numbers) # [1, 2, 4, 5, 5, 7]
# numbers = [5, 2, 1, 5, 7, 4]
# numbers.sort()
# numbers.reverse()
# print(numbers)  # [7, 5, 5, 4, 2, 1]
# numbers = [5, 2, 1, 5, 7, 4]
# numbers2 = numbers.copy()
# numbers.append(10)
# print(numbers2) # [5, 2, 1, 5, 7, 4]


# Exercise: Write a program to remove the  duplicates in a list

# numbers = [2, 2, 4, 6, 3, 4, 6, 1]
# uniques = []
# for number in numbers:
    # if number not in uniques:
        # uniques.append(number)
# print(uniques)   # [5, 2, 1, 5, 7, 4]



#Tuples
# numbers = (1, 2, 3)
# numbers[0] = 10
# print(numbers[0])


#Unpacking 

# coordinates = (1, 2, 3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
# x, y, z = coordinates # same as above
# print(x) # 1 
# print(y) # 2
# print(z) # 3

# coordinates = [1, 2, 3]
# x, y, z = coordinates
# print(y) # 2



#Dictionaries
# Name: John Smith  # key:value pairs
# Email: john@gmail.com
# Phone: 1234

# customer = {
    # "name": "John Smith",
    # "age": 30,
    # "is_verified": True
# }
# print(customer["name"]) # John Smith
# print(customer["birthdate"]) # KeyError: 'birthdate'
# print(customer["Name"]) # KeyError: 'Name'
# print(customer.get("birthdate")) # None
# print(customer.get("birthdate", "Jan 1 1980")) # Jan 1 1980
# customer["name"] = "Jack Smith"
# print(customer["name"]) # Jack Smith
# customer["birthdate"] = "Jan 1 1980"
# print(customer["birthdate"]) # Jan 1 1980

# EXERCISE: 
# Phone: "1234"
# "1" -> "One"
# "2" -> "Two"
# phone = input("Phone: ")
# digits_mapping = {   # the dictionary 
    # "1": "One",
    # "2": "Two",
    # "3": "Three",
    # "4": "Four"
# }
# output = ""  # here its the variable we will print for the terminal
# for ch in phone:
    # output += digits_mapping.get(ch, "!") + " " #key value from character which are 1, 2, 3, 4 and key values being one, two, three, four. and the " " for space between words while iterating
# print(output) # if we write on the Phone:1234 => One Two Three Four  or if we type 1267  => One Two ! !


# Emoji Converter :)
# message = input(">")
# words = message.split(' ') 
# print(words)
# emojis = {
    # ":)": "🙂",
    # ":(": "😔" 
# }
# output = ""
# for word in words:
    # output += emojis.get(word, word) + " "
# print(output)


# Functions
# def greet_user():
    # print('Hi there!')
    # print('Welcome aboard')


# print('Start') 
# greet_user()
# print('Finish')   

# output: Start
# Hi there!
# Welcome aboard
# Finish


# Parameters
# def greet_user(name):
    # name = "John" ; name inside function act like this because we set the variable inside the parenthesis.
    # print(f'Hi {name}!')
    # print('Welcome aboard')


# print('Start') 
# greet_user('John')
# greet_user('Mary')
# print('Finish')   

# output: Start
# Hi John!
# Welcome aboard
# Hi Mary!
# Welcome aboard
# Finish

# def greet_user(name):
    # name = "John" ; name inside function act like this because we set the variable inside the parenthesis.
    # print(f'Hi {name}!')
    # print('Welcome aboard')


# print('Start') 
# greet_user()
# greet_user('Mary')
# print('Finish')   

# output: TypeError: greet_user() missing 1 required positional argument: 'name'



# def greet_user(first_name, last_name): 
    # print(f'Hi {first_name} {last_name}!')
    # print('Welcome aboard')


# print('Start') 
# greet_user('John', 'Smith')
# print('Finish') 

# output : Start
# Hi John Smith!
# Welcome aboard
# Finish


# Keyword Arguments 
# def greet_user(first_name, last_name): 
#     print(f'Hi {first_name} {last_name}!')
#     print('Welcome aboard')


# print('Start') 
# greet_user('John')
# print('Finish') 

# output: TypeError: greet_user() missing 1 required positional argument: 'last_name'


# def greet_user(first_name, last_name): 
#     print(f'Hi {first_name} {last_name}!')
#     print('Welcome aboard')


# print('Start') 
# greet_user('Smith','John')
# print('Finish') 

# output: Start
# Hi Smith John!
# Welcome aboard
# Finish


# def greet_user(first_name, last_name): 
#     print(f'Hi {first_name} {last_name}!')
#     print('Welcome aboard')


# print('Start') 
# greet_user(last_name='Smith', first_name='John')
# calc_cost(total=50, shipping=5, discount=0.1)
# print('Finish') 

# terminal: Start
# Hi John Smith!
# Welcome aboard
# Finish


# Return Statements 

# def square(number):
    # return(number * number)
# result = square(3)
# print(result)
# print(square(3))
# terminal: 9

# def square(number):
#     print(number * number)
#     # if we dont use "return" in a definition python will return "None". So all the functions in Python return "None". So to return something you should use the return statement.
# print(square(3))


# Creating a Reusable Function

# def emoji_converter(message):
#     words = message.split(' ') 
#     print(words)
#     emojis = {
#         ":)": "🙂",
#         ":(": "😔" 
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output  # usually without a function it would be the last line as "print(output)" but in this case we should include it in the function as "return output".


# message = input(">")
# print(emoji_converter(message))


# Exceptions
 
# age = int(input('Age: '))
# print(age)
# if we type 20 the terminal will return 20.
# when entering characters of alphabet like : "asd" we get a value error =>  ValueError: invalid literal for int() with base 10: 'asd'

# try:
#     age = int(input('Age: '))
#     income = 20000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print('Age cannot be 0.')
# except ValueError: 
#     print('Invalid value')



# Comments

# Bad comment: Sky is blue - it's telling us the obvious
# print('Ocean is blue')

# # Bad comment: Calculates and returns the square of a number
# def square(number):
#     return number * number

# Tip: use comments to explain why's and how's, not what's ; explain assumptions or add notes to remind you to do something in the code



# Classes 

# Numbers
# Strings
# Booleans
# ---
# Lists
# Dictionaries

# class Point:   #we use pascal case on classes
#     def move(self):
#         print("move")
    
#     def draw(self):
#         print("draw")


# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.move()
# point1.draw()

# point2 = Point()
# point2.x = 1
# print(point2.x)



# Constructors


# class Point:   
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def move(self):
#         print("move")
    
#     def draw(self):
#         print("draw")

# point = Point(10, 20)
# point.x = 11
# print(point.x)


# Person 
# -name 
# -talk()

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def talk(self):
#         print(f"Hi, I am {self.name}")


# john = Person("John Smith")
# john.talk()

# bob = Person("Bob Smith")
# bob.talk()



# Inheritance - the dog and cat class will inherit the attributes of the parent class Mammal

# class Mammal:
#      def walk(self):
#         print("walk")


# class Dog(Mammal):
#     # pass # means nothing or dont worry about it    
#     def bark(self):
#         print("bark")

# class Cat(Mammal):
#     def be_annoying(self):
#         print("annoying")
    
# dog1 = Dog()
# dog1.walk()

# cat1 = Cat()
# cat1.be_annoying()




# Modules

# def lbs_to_kgs(weight):
#     return weight * 0.45

# def kg_to_lbs(weight):
#     return weight / 0.45

# import converters

# print(converters.kg_to_lbs(70))  # result: 155.55555555555554

# import converters
# from converters import kg_to_lbs 

# kg_to_lbs(100)

# print(converters.kg_to_lbs(70))


# EXERCISE 

# from utils import find_max

# numbers = [10, 3, 6, 2]
# maximum = find_max(numbers)
# print(maximum)


# Packages

# import ecommerce.shipping 

# ecommerce.shipping.calc_shipping()  # terminal: calc_shipping



# from ecommerce.shipping import calc_shipping

# calc_shipping()    # terminal: calc_shipping



# from ecommerce import shipping

# shipping.calc_shipping()




# Generating Random Values

# import random 

# for i in range(3):
#     print(random.random()) # for instance the terminal will display: 0.7214185066115757
                                                                    #  0.5171827849315377
                                                                    #  0.32454296452605513


# import random

# for i in range(3):
#     print(random.randint(10,20)) # it will randomly display on terminal 18, 13, 11 for instance


# import random

# members = ['John', 'Mary', 'Bob', 'Mosh']
# leader = random.choice(members)
# print(leader) # it will randomly generate a name inside the list 'members' so it could be John/Mary/Bob/Mosh


# import random


# class Dice:
#     def roll(self):
#         first = random.randint(1,6)
#         second = random.randint(1,6)
#         return first, second


# dice = Dice()
# print(dice.roll())  # it will randomly generate numbers from 1-6 eg. (1,1) or (6,5) everytime you run it.




# Files and Directories

# Absolute path 
# c:\Program Files\Microsoft - Windows
# /usr/local/bin - Mac or Linux
# Relative path

from pathlib import Path

# path = Path("ecommerce")
# print(path.exists())  # True

# path = Path("ecommerce1")
# print(path.exists())  # False

# path = Path("emails")
# print(path.mkdir())    # None  -- and it adds a directory


# path = Path("emails")
# print(path.rmdir())     # None -- and it deletes a directory


# path = Path("ecommerce")
# print(path.exists())  # True

from pathlib import Path

path = Path()
print(path.glob('*.*'))    # * all files ; *.* in the current directory , '*.py'
 