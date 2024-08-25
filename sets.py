# sets
empty_set = set()
sample_set = {"a", "b", "c", 1, 2, 3, True}

# Add
sample_set.add("added_element")

print(sample_set)
for item in sample_set:
    print(item)

# set operations

s1 = {"foo", "bar", "baz"}
s2 = {"baz", "qux", "quux"}
print(s1.union(s2))

print(s1.difference(s2))

print(s1.symmetric_difference(s2))

s3 = {"a", "b", "c", "d", "e"}
s4 = {"a", "b"}
print(s4.issubset(s3))

# Removing duplicates
l1 = [1, 2, 3, 4, 5, 6, 2, 7, 4, 9, 5, 6]
print(list(set(l1)))