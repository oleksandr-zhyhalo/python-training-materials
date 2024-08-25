# tuple is not modifiable after creation
from opcode import cmp_op

tup1 = (1,2,3,4,5)
tup2 = 1,2,3,4,5,6
tup3 = tuple(["a","b", "c"])
creds = ("login", "password")

print(tup1[1])

# This will be TypeError
# tup1[0] = 42

# Removing a tuple element
# del tup2[-1]

tup4 = tup1 + creds
print(tup4)
sample_tuple = ("Hi",)

# Repetition
print(sample_tuple*4)

# Conditionals
if 2 in tup2:
    print("Found")
else:
    print("Not found")

# Build in functions for tuples
print(len(tup3))
print(min(tup1))
print(max(tup2))