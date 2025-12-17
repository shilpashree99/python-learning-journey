🐍 Python Variables
📌 Introduction

In Python, variables are used to store data that can be referenced and manipulated during program execution.
A variable is essentially a name assigned to a value.

Unlike languages such as Java, Python does not require explicit type declaration.
The type of a variable is automatically inferred at runtime based on the assigned value.

🔹 Creating Variables
Example:
x = 5
name = "Samantha"

print(x)
print(name)

Output:
5
Samantha

🔹 Rules for Naming Variables

To use variables effectively, Python enforces the following rules:

Variable names can contain letters, digits, and underscores (_)

Variable names cannot start with a digit

Variable names are case-sensitive (myVar and myvar are different)

Python keywords (e.g., if, else, class, for) should not be used as variable names

✅ Valid Variable Names
age = 21
_colour = "lilac"
total_score = 90

❌ Invalid Variable Names
1name = "Error"      # Starts with a digit
class = 10           # Reserved keyword
user-name = "Doe"    # Hyphen is not allowed

🔹 Assigning Values to Variables
Basic Assignment

Variables are assigned values using the = operator.

x = 5
y = 3.14
z = "Hi"

🔹 Dynamic Typing

Python is a dynamically typed language, meaning the same variable can hold values of different data types during execution.

x = 10
x = "Now a string"

🔹 Multiple Assignments
Assigning the Same Value

Python allows assigning the same value to multiple variables in a single line.

a = b = c = 100
print(a, b, c)


Output:

100 100 100

Assigning Different Values

Multiple variables can be assigned different values simultaneously.

x, y, z = 1, 2.5, "Python"
print(x, y, z)


Output:

1 2.5 Python

🔹 Type Casting in Python

Type casting is the process of converting one data type into another.
Python provides built-in functions such as:

int() → converts to integer

float() → converts to floating-point number

str() → converts to string

Example:
s = "10"
n = int(s)

cnt = 5
f = float(cnt)

age = 25
s2 = str(age)

print(n)
print(f)
print(s2)


Output:

10
5.0
25

🔹 Getting the Type of a Variable

The type() function is used to determine the data type of a variable.

n = 42
f = 3.14
s = "Hello, World!"
li = [1, 2, 3]
d = {'key': 'value'}
flag = True

print(type(n))
print(type(f))
print(type(s))
print(type(li))
print(type(d))
print(type(flag))


Output:

<class 'int'>
<class 'float'>
<class 'str'>
<class 'list'>
<class 'dict'>
<class 'bool'>

🔹 Deleting a Variable Using del

The del keyword removes a variable from memory.

x = 10
print(x)

del x
# print(x)  # This will raise NameError

Explanation:

del x removes the variable x from the namespace

Accessing x after deletion raises a NameError

✅ Summary

Variables store data values

Python uses dynamic typing

Variable naming rules must be followed

Supports multiple assignments

Type casting converts data types

type() checks variable data type

del deletes variables from memory