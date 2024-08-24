[]
list()

arr1 = [1, 2, 3, 45, -1, -3]
arr2 = ["a", "b", "c"]
mixed_arr = [1, 2.3, "string", True, None]
nested_list = [[1, 2, 3], ["a", "b", "c"]]

firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita"]
# take first element
print(firstnames[0])
# take last element
print(firstnames[-1])
# find len of list
print(len(firstnames))
# Listing indexes
for index in range(len(firstnames)):
    print(index)
# Working with elements
for firstname in firstnames:
    print(firstname[-1])

# Modifying a list
firstnames.append("Oggy")
firstnames.append("Tom")
firstnames.sort()

# print(firstnames)

firstnames.insert(6, "Marta")
# print(firstnames)

firstnames_female = ["Ewa", "Anita"]
firstnames_male = ["Adam", "Marcin", "Krzysztof", "Jakub", "Adam", "Jakub"]
firstnames = firstnames_female + firstnames_male


# Removing by index
#del firstnames[-1]
print("----" * 5)

# Remove by value first occurrence
# firstnames.remove("Jakub")
# print(firstnames)

# remove the duplicates by dict conversion
# firstnames = list(set(firstnames))

# Funny solution
# while "Jakub" in firstnames: firstnames.remove("Jakub")

# Find index by value
# print(firstnames.index("Adam", 3, 5))
print(firstnames)

# Conditionals with lists
if "Jakub" in firstnames:
    print("Jakub found")
else:
    print("Jakub not found")

if "Boris" not in firstnames:
    print("Boris never found!")

empty_list = [""]

if empty_list:
    print("List is not empty")
else:
    print("List is empty")