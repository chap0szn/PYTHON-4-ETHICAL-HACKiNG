# this line i running python without a variable.
print('hello world')
print("i am learning python programming language")

# Declaring a variablee
f_name = "Destiny"
l_name = "Okpalaji"


# Concatenating a variablee
print(f_name + " " + l_name)

age = 18
sentence = "is the legal age age to vote in "
country = "Nigeria"

print(str(age) + " " + sentence + country)

# # Today's class (Friday's class)
# # Dictionationary is a collection of key-value pairs
# # Example of a dictionary
# cars = {'BMW': 'X6', 'Mercedes': 'GLC300', 'Tesla': 'Model X', 'Audi': 'Q3'}
# print(cars['Mercedes'])

# # List is a collection of items
# fruits = ['orange', 'bannana', 'apple', 'pineapple', 'mango', 'grep']

# # Calling item in a list by their index number
# # Indexing starts from 0
# # Example of indexing
# # fruits[0] = 'orange'
# # fruits[1] = 'bannana'
# # fruits[2] = 'apple'
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])
# print(fruits[4])
# print(fruits[5])
# print(fruits[1:5])

# # Builtin function to add item
# fruits.append('test')

# # Remove an item
# fruits.remove('mango')
# print(fruits)

# # looping through an item multiple time using for statement
# # identation works with control flow
# # for fruits in fruits:
# #     print(fruits)

# # print an item in ranges
# for i in range(5):
#     print(fruits)

# # comment out with short cut (ctrl + /)

# # Looping through a line of code using while statement
# count = 0
# while count <= 100:
#     print("count: ", + count)
#     count += 2 # increment

# # dEFINING A FUNCTION
# def new_function(sum): # Parameter
#     return sum

# print(4+4) # value


# # name = input("What is your name: ")
# # print("My name is " + name)

# change_ip = input("Type your IP addr: ")
# print("Your IP has been changed to " + change_ip)


# Class on Tuesday - 08/04/2025)
# 1. Functions

# Creating a function
def greet():
    print("Good morning")

# Calling a function
greet()

# Pass an argument to a function
def greet(name):
    print("Good morning " + name)

# Passing an argument to a function
greet("Ephraim")
greet("Norbert")
greet("Juma")

# A parameter is a variable in a function definition
# An argument is the value you pass to a function when you call it
# Function with multiple parameters

def greet(f_name, l_name):
    print("Good morning " + f_name + " " + l_name)

# Calling a function with multiple parameters
greet("Ephraim", "Norbert")
greet("Juma", "Mwanakombo")

# Python Try Except
# Handling exceptions
# The 'try' block lets you test a block of code for errors
# The 'except' block lets you handle the error
# The 'else' block lets you execute code when there is no error
# The 'finally' block lets you execute code regardless of the result of the try-except block

# Example of try except
try:
    print(x) # This will cause an error because x is not defined
except:
    print("An error occurred") # This will be executed if there is an error

# Many exceptions
try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("something else went wrong")

    #Else statement
    #Else is executed when there is an error
