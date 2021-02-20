'''
Notes on Functions...

'''

# Defining a function

# 1 Parameter
def greeting(name):
    print("Welcome, " + name)

greeting("Pythonista")
# 2 Parameters
def greeting2(name, department):
    print("Welcome, " + name)
    print("You are part of " + department)

greeting2("Pythonista", "Engineering")

'''
Definig Custom Functions:
- Use the 'def' keyword

example: def my_function():
            #Code goes here; remember to indent...

- We can add paramters to our functions like so:

example: def my_function(param1, param2):
                # params used inside of the code block...

- A function can have NO paramters. 

- A Function can have multiple paramters.

- Parameters allow us to call a function and pass data into it.

Fully Developed Function:

def my_function(param1, param2):
        return param1 + param2

Make sure that your indenting is consisten...

So if you use 2 spaces, use 2 spaces

If you use 4 spaces (tab) then use 4 spaces...

Make sure this is consistent all throughout your code.
'''

# Returning Values

def area_of_triangle(base, height):
    return (base * height)/2

area_of_triangle(5,10)

area_a = area_of_triangle(5,4) # Can use a function inside of a variable.

area_b = area_of_triangle(7,9) # Can hold the values returned from a function within that variable.

sum = area_a + area_b # Can print the sum of those 2 variables now that we can hold the values from those calculations within a variable.

print(sum) # Printing out that sum...

# By creating functions like this we can make our code more reusable...

# We can assign multiple variables to a function that can return multiple varibales...

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000) # Because the function returns 3 different values, we can define 3 different variables.

print(hours, minutes, seconds) # You cannot just ask for one value back (or at least I think you can't)

# If you print each one individually, you get back the array (list)...

# None: A special data type in Python used to indicate that things are empty or that they returned nothing. 

def get_name(): # if you add a paramter you won't be able to get input because Python is looking for that positional paramter...
    name = input("What is your name? ")
    return name

user_name = get_name()

print(user_name)

def get_department():
    department = input("What is your department? ")
    return department

user_department = get_department()

def greetings(name, department):
    print(f"Welcome, {name}! Your department is {department}.")

print(user_department)

welcome_user = greetings(user_name, user_department) # Using values we got from the previous 2 functions to create the function we had in the beginning. 

# I like this because you can 'atomize' your functions and then bring it all back together so that you can work with those functions and your code ina  more granular, repeatable way.

print(welcome_user)

'''
Returning Values Using Functions

- Can use functions to manipulate data we pass it and return the value to use.
- Use the 'return' keyword to return values back to the user. 
- We can call the function and store the value inside of a variable.
- Return values allow the functions to be more flexible and powerful so they can be reused and called many times. 
- Functions can return mutliple values
    - Remember to store all returned values into variables!
        - If you don't, then it will return all the values as an array (list)
- A function can also return 'nothing'; the function just exits.
    - Will get a None type.
    - Tells us that a function has not returned anything
'''

# Messing around with the len() function...

def get_username_length():
    print("Please choose a username between 1 and 10 characters long.")
    username = input("Enter a username: ")

    if len(username) < 1:
        return print(f"Username is not long enough! Your username is {str(len(username))} characters long.")
    elif len(username) > 10:
        return print(f"Username is too long! Your username is {str(len(username))} characters long.")
    #elif username == None:
        #return print("There was no username entered!") --> Couldn't get to work right...
    else:
        return print(f"Your username is {username} and it is {str(len(username))} long.")
    
    return username

length_of_username = get_username_length()

print(length_of_username)

# Principals of Code reuse

'''
This section talks about reducing code duplication and DRY priniciples...
'''

name = input("What is your name?")
print(f"Hello {name} your lucky number is {len(name)*9}")

# We can make this better...

def lucky_number(name):
    number = len(name) * 9
    print(f"Hello {name}. Your lucky number is {number}.")

lucky_number("Guy")

# Code Style

''' 
Good style helps users be able to read your code. 

Good style makes life easier for people who have to maintain the code

Reduces errors

Code Style doesn;t matter to the computer, this is just for readers of your code

Principles:
1. You want your code to be as self-documenting as possible. 

Self-Documenting Code: Written in a way that's readable and doesn't conceal its intent. 

- Clear varibales and functions

Refactoring: The practice of cleaning up code to make it more clean and readable and useful.

When you cannot make variables and code clear, make sure you use comments to comment what the code is doing. 

Try to use a style guide when you are writing code.
'''