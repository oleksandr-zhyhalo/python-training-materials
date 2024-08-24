# While loop
# while condition is true:
#   code_line_1

# Simple loop
counter = 0
while counter < 10:
    counter += 1
    if counter == 5:
        continue
    print(f"{counter}: Hello")

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


# break inside loop
# while true:
#   linux_command check if process exists:
#       perform_some_action
#       break
#   wait(10)


# program that prints the factorial
counter = 0
product = 1
while counter < 11:
    counter += 1
    product *= counter
    if product > 1000:
        print(f"Exiting loop due to product being more than 1000")
        break
    print(f"{counter}: {product}")

# continue inside loop
# while true:
#   if website_is_down:
#       send_notification_to_email
#       continue
#   print everything_is_fine > app.log
#   wait(10)

# Continue example
counter = 0
while counter < 10:
    counter += 1
    if counter == 3:
        print("Everything after continue now will be skipped")
        continue
    print(counter)


#For loops
for i in range(0,6):
    print(f"Loop 1: {i}")
for i in range(2,6):
    print(f"Loop 2: {i}")

for i in range(10, 100, 10):
    if i == 40 or i == 50:
        break
    print(f"Loop 3: {i}")

arr = [
    [["a", "b", "c"], ["a", "b", "c"], ["a", "b", "c"]],
    [["a", "b", "c"], ["a", "b", "c"], ["a", "b", "c"]],
    [["a", "b", "c"], ["a", "b", "c"], ["a", "b", "c"]],
]
print(f"First element: {arr[0]}")
print(f"Second element: {arr[1]}")

counter = 0

for i in arr:
    for j in i:
        for k in j:
            if k == "a":
                counter +=1
print(counter)

