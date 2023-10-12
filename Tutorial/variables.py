# Creating Variables

x = 5
y = "John"
print(x) # 5
print(y) # John 
         
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)    # Sally

            
# Casting

x = str(3)    # if we print x, it will be '3'
y = int(3)    # if we print y, it will be 3
z = float(3)  # if we print z, it will be 3.0


# Get the Type

x = 5
y = "John"
print(type(x))  # class'int'
print(type(y))  # class'str'


# Single or Double Quotes?

x = "John"           # is the same as
x = 'John'           # İf we print x, it prints "John" in two situation.

# Case-Sensitive

a = 4
A = "Sall"  # A will not overwrite a



# Variable Names

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"   # All of them prints "John"

2myvar = "John"
my-var = "John"
my var = "John"   # It gives error.



# Multi Words Variable Names

# Camel Case
myVariableName = "John" 

# Pascal Case
MyVariableName = "John" 

# Snake Case
my_variable_name = "John"



# Assign Multiple Values

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)  # Orange
print(y)  # Banana
print(z)  # Cherry

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)  # Orange
print(y)  # Orange
print(z)  # Orange

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)  # apple
print(y)  # banana
print(z)  # cherry


# Output Variables

x = "Python is awesome"
print(x)  # Python is awesome

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)  # Python is awesome

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)  # Python is awesome

x = 5
y = 10
print(x + y)  # 15

x = 5
y = "John"
print(x + y)  # It gives error.

x = 5
y = "John"
print(x, y)   # 5 John


# Global Variables

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()   # Python is awesome

    x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)  # Python is fantastic

myfunc()

print("Python is " + x)    # Python is awesome

# The global Keyword

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)  # Python is fantastic


x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)  # Python is fantastic

