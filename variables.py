# Variable names
myvar = "something"
_myvar = "something"
_my_var = "something"
myVar = "something"
myvar2 = "something"

# Illegal variable names
# 2var="something"
# my-var = "something"
# my var = "something"


# Main variable types
# age = 23 # Integer or int
# Name = "Jakob" # String or str
# height = 1.73 # Floating point number or float
# isFemale = True # Boolean or bool
# var3 = None

# Variables arithmetic operation
# a = 2
# b = 19
# print(a + b) # Addition
# print(a - b) # Substructure
# print(a * b) # Multiplication
# print(b / a) # Division
# print(a ** b) # Exponentiation
# print (b % 2) # Modulus
# print(b // a) # Floor division

# Variables assignment operation
# b //= 5

# Boolean Operation
a = 5
b = 6
c = 10
# Equal
print(a == b)
print(b == a)
print(a == c)
# Not equal
print(a != b)
print(a != c)
# Greater equal then
# Smaller equal then
print("*"*10)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)

# Logical operations
print("*"*10)
var1 = True
var2 = True
var3 = False
var4 = False

print(1==1 and 2==3) # and operator
print(False or False or False or True) # or operator
print(not False == True) # not operator
print("*"*10)

# Different boolean values
print(bool(-1))
print(bool(10))
print(bool(0))

print(bool(1.2))
print(bool(-5.3))
print(bool(0.0))

# Different boolean values with string
print("*"*10)
print(bool("hello"))
print(bool(""))
print(bool(" "))
print(bool(None))

# Checking variables type
print("*"*10)
age = 23 # Integer or int
name = "Jakob" # String or str
height = 1.73 # Floating point number or float
isFemale = False # Boolean or bool
var3 = None

print(type(age))
print(type(name))
print(type(height))
print(type(isFemale))
print(type(var3))

# Casting a variables
print("*"*10)
age = float(age)
b = int(44.99)
print("Value: {}, Type: {}".format(b, type(b)))

