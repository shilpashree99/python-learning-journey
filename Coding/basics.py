"""
Day 1: Python Basics
Author: Shilpashree
Topics: Variables, Strings, Input/Output, Data Types, Keywords
"""

# -----------------------------
# Variables and String Concatenation
# -----------------------------
first_name = "shilpashree"
last_name = "S R"

full_name = first_name + " " + last_name
print("Full Name:", full_name)

# -----------------------------
# String Repetition
# -----------------------------
message = "This is a Warning!\n"
print("Message Repetition:")
print(message * 5)

# -----------------------------
# String Methods
# -----------------------------
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Stripped & Repeated:", message.strip() * 2)

rep_mes = message.replace("Warning", "Error")
print("Replaced Message:", rep_mes)

# -----------------------------
# Multiline String
# -----------------------------
family_members = '''
My name is Shilpashree,
My father is Ramanjinappa,
and my mother is Gangarathnamma
'''
print("Family Members:")
print(family_members)

# -----------------------------
# Basic Print
# -----------------------------
print("Hello World!!")

# -----------------------------
# Comments
# -----------------------------
# This is a single-line comment

"""
This is a multi-line comment
using triple quotes
"""

# -----------------------------
# User Input
# -----------------------------
string_input = input("Enter a value (string): ")
integer_input = int(input("Enter an integer value: "))
print("You entered:", string_input, integer_input)

# -----------------------------
# Multiple Inputs
# -----------------------------
x, y = input("Enter 2 values: ").split()
print("Two values:", x, y)

a, b, c = input("Enter 3 values: ").split()
print("Three values:", a, b, c)

color = input("Enter color of leaf: ")
print("Leaf color:", color)

price = float(input("Enter price of rupee: "))
print("Price:", price)

# -----------------------------
# Data Types
# -----------------------------
a = 5
b = 5.0
c = 'Five'
d = ("Five", "Rupees")
e = ["Five", "Rupees"]
f = {"Five": 5, "Rupee": 6}

print("Data Types:")
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

# -----------------------------
# Multiple Variable Printing
# -----------------------------
x = 5
name = "samantha"
print(x, name)

# -----------------------------
# Valid Variable Names
# -----------------------------
age = 21
_color = "Red"
total_score = 98
print(age, _color, total_score)

# -----------------------------
# Assigning Values
# -----------------------------
x = 5
y = 5.5
z = "hi"
print(x, y, z)

# -----------------------------
# Dynamic Typing
# -----------------------------
x = 10
x = "shilpa"
print("Dynamic Typing:", x)

# -----------------------------
# Multiple Assignment
# -----------------------------
a = b = c = 10
print(a, b, c)

a, b, c = 10, 20, 30
print(a, b, c)

# -----------------------------
# Python Keywords
# -----------------------------
import keyword
print("Python Keywords:")
print(keyword.kwlist)
