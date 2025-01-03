
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

print(f"{user_name} is {user_age} years old. His interests include {user_interests}.")

