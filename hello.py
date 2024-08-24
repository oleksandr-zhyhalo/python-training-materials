# Text manipulation
age = 24
var2 = 2.32535423352
name = "Oleksandr"
print("Hello anything, 12390, *10")
print("Hello " + "World")
print("Hello " * 10)
#####
#print("I am %s years old and again my age is %s" % (age, age)) # Old method and it's deprecated

# Format method
# print("I am {a} year old and my name is {b}. {b} is my real name".format(a=age, b=name))

# Shorthand method
print(f"I am {age} years old, my name is {name}.")

# Float rounding
print("%.2f" % 1.2399) # returns "1.24"
print(f"{round(var2,2)}")

# Escaping
print("My name is \"Oleksandr\"")

# New line
print(f"Name: {name}\nAge: {age}")
