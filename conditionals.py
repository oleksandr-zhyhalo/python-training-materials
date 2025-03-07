"""
if statement
if (conditional) {
code_line1;
code_line2;
}
"""
# if indentation
if False:
    print(1)
    print(2)
    print(3)
print(4)

# If conditions
if 1 == 1 and 2 == 3:
    print("Condition is satisfied")

if 1 == 1 or 2 == 3:
    print("Condition is satisfied")

c = "Sample text"
if c:
    print(f"c exists, and value of c is {c}")
c = ""
if c:
    print(f"c exists, and value of c is {c}")


# Check if number is odd or even
num = 7
if num % 2:
    if num > 10:
        print(f"Number {num} is odd and > 10")
    else:
        print(f"Number {num} is odd and < 10")
else:
    print(f"Number {num} is even")


# FizzBuzz task
# number is dividable by 5 - print Fizz, and if dividable by 3 print Buzz. If both print FizzBuzz.
# 15 = 3*5. Means, that every number that can be divided by 15, also can be divided by 5 or 3.
print("Please enter a number:")
number = int(input())

if not number % 15:
    print("FizzBuzz")
elif not number % 5:
    print("Fizz")
elif not number % 3:
    print("Buzz")
else:
    print(f"Number {number} is not dividable by 3 or 5")


# elif
# if conditions is false:
# elif condition is false:
# elif conditions is true:
#   line_of_code
# else: