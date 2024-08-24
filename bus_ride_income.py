"""
A simple program that takes the age of all passengers on a bus.
The cost of a child's ticket is PLN 200, the cost of an adult ticket is PLN 400.
If the passenger is an adult, he can also order alcohol (maximum 3 glasses of wine, each for PLN 10).
There can be a maximum of 20 passengers. The program calculates the total revenue from tickets.
If the age of the passenger is 0 or the maximum number of passengers has been reached, the program exits printing the summary:
Total revenue, Number of Adult Passengers, Number of Children, Number of Wine Glasses.
"""
wine_count = 0
child_count = 0
adult_count = 0
passenger_count = 0

while passenger_count < 20:
    print("Please enter age: ")
    age = int(input())
    if age <= 0:
        break
    elif age < 18:
        child_count += 1
        passenger_count += 1
        continue
    print("Enter number of glasses o wine: ")
    wine_current = int(input())
    while wine_current < 0 or wine_current > 3:
        print("Wrong number of glasses")
        print("Enter number of glasses o wine: ")
        wine_current = int(input())
    wine_count += wine_current
    adult_count += 1
    passenger_count += 1
print(
    f"Adults: {adult_count}\nChild: {child_count}\nWine Glasses: {wine_count}\nIncome: {adult_count * 400 + child_count * 200 + wine_count * 10}")
