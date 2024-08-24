# While loop
# while condition is true:
#   code_line_1

#Smple loop
# counter = 0
# while counter < 10:
#     counter += 1
#     print(f"{counter}: Hello")

# Write a code if number is a prime.
print(f"Input a number:")
number = int(input())

x = number // 2
factor = 0
while x > 1:
    if number % x == 0:
        print(f"{number} has factor {x}")
        factor = x
    x -= 1
if not factor:
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")

