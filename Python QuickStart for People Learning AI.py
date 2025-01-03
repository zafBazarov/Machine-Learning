
# Python for People Learning AI [Mini-Course]

# Beginner friendly- QuickStart Guide.

# This lesson is created by Sha Talebi. This link is for original source: https://youtu.be/pNg2DJ4spXg?si=XWMjtiCOuiDzBToq

# Introduction

# What is Python (Programming Language)?
# Python is a programming language which is simply a way to give computers precise instructions to do things we can't or don't want to do. 

# Coding is Easier Than Ever - Thanks to Google and ChatGPT

# This tutorial is for Who
  # learning AI + some coding, but new to Python

### Python Basics

## Data Types
    # A way to classify data to process it appropriately and efficiently
# Text 
      # Strings = chracter sequences e.g. "Hello", "He11o!"
         a = 'This is a tring' # no difference between ' and " quotation nut
         b = 'Zafar said "Python is awesome!"' # here " may cause an error 

# Numbers
        # Ints = integers e.g. 1,2, 42
          integer = 1
        # Floats = numbers with decimals e.g. 1.0, 1.34
          float = 3.41

# Lists = ordered collection of values
          lst1 = ['a', 'b', 'c']  # a list of strings

          lst2 = [1, 2, 3]        # a list of ints

          lst3 = ["a", 1, 3.14]   # list with string, int and float

          lst4= [["a","b"], [1, 2], [2.2, 3.3]] # list of lists

## Dictionaries = key-value pair sequences
    # It is a bit different than list so instead of the square brackets we have curly brackets {}. Also we have key value pairs  where each item in the dictionary consists two parts a key which will always be a string and a value whcin can be any data type. 
    # A sing dictionary might have a singe item with a key called name and a value of name.

# a dictionary
{"Name": "John"}

# a dictionary with multiple key-value pairs
 {"Name": "John", "Age":29, "Interests":["AI", "Music", "Bread"]}

# We can also combine a list in dictionary data types. 

# a list of dictionaries
[ {"Name": "John", "Age":29, "Interests":["AI", "Music", "Bread"]}, 
 {"Name": "Shaw", "Age":27, "Interests":["Marketing", "YouTube", "Shopping"]} ]

# we can also have a dictionary within a dictionary the way that looks is we might have a key value pair corresponding to a user and the value for this item will be another dictionary which includes user information then the other items in the dictionary might be the last login date and the membership tier of user.

# a nested dictionary
{"User": {"Name": "John", "Age":29, "Interests":["AI", "Music", "Bread"]},
 "Last_login": "2025-01-01",
 "Membership_Tier": "Free"}

## Variables = are abstract representation of underlying data. It gives to make coding a bit easier. This helps us avoid writing John over and over again.

# creating a variable and printing it
user_name = "John"
print(user_name)

# We can also define multiple variables and use them to print a specific text. When writing Python scripts, this gives us more flexibility.
# defining more variables and printing them as a formatted string. 
user_age = 29
user_interests = ["AI", "Music", "Bread"]

print(f"{user_name} is {user_age} years old. His interests include {user_interests}.")  # f is the formatted string


## Loops & Conditions

# Loop runs a chunk of code multiple times. 

# for loop - it is the most popular loop
# a simple for loop iterating over a sequence of numbers
for i in range(5): 
  print(i)  # print i the element

# We can also iterate over items in a list.

# for loop iterating over a list
user_interests = ["AI", "Music", "Bread"]

for interest in user_interests:
  print(interest)   # rpint each items in list

# It is alos possible to iterate over items in a dictionary

# for loop iterating over items in a dictionary
user_dict = {"Name": "John", "Age":29, "Interests":["AI", "Music", "Bread"]}

for key in user_dict.keys():
    print(key, "=", user_dict[key]) # print each key and corresponding value


# Conditions is a program logic

# if-else statements

# check if user is 18 or older
if user_dict["Age"] >=18:
  print("User is an adult")


# we can also have 'else'. if the value is not true we can have do another command using else.

# check if user is 1000 or older, if not print they have much to learn
if user_dict["Age"] >=1000:
  print("User is wise")
else:
  print("User has much to learn")


# Bringing Loops and Conditions together

# for loop + if statement

# count the number of users interested in bread
user_list = [ {"Name": "John", "Age":29, "Interests":["AI", "Music", "Bread"]}, 
              {"Name": "Shaw", "Age":27, "Interests":["Marketing", "YouTube", "Shopping"]} ]
count = 0 # initialize count

for user in user_list:
  if "Bread" in user["Interests"]:
      count = count + 1     # update count

print(count, "user(s) interested in Bread")


## Functions
# Fuctions are operations we can perform on specific data types. 

# print() fiúnctions - prints our data
print(user_list)

# type(), getting the data type of a variable
get(user_list)

# len(), getting the length of a variable. But it is not for integers it works only with strings
len(user_list)   # len() works with only strings not integers

user_interests = ["AI", "Music", "Bread"]
print(len(user_interests))  # the result is 3 because we have only there interest in the list

## string methods
# make string all lowercase
print(user_dict["Name"].lower())

# make string all uppercase
print(user_dict["Name"].upper())

# split string into list based on a specific character sequence
print(user_dict["Name"].split("ha"))

# replace a character sequence with another
print(user_dict["Name"].replace("w", "whin"))


## list methods

# add an element to the end of a list
user_dict["Interests"].append("Entrepreneurship")
print(user_dict["Interests"])

# remove a pecific element from a list
user_dict["Interests"].pop(0)   # 0 is the order number of an element
print(user_dict["Interests"])      

# insert an element into a specific place in a list
user_dict["Interests"].insert(1, "AI") # 1 is the order number of an element
print(user_dict["Interests"])


## dictionary methods

# accessing dict keys
print(user_dict.keys())

# accessing dict values
print(user_dict.values())

# accessing dict items
print(user_dict.items())

# aremoving a key
user_dict.pop("Name")
print(user_dict.items())

# adding a key
user_dict["Name"] = "Shaw"
print(user_dict.items())
