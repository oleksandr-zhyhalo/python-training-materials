# Dicts are main data type
# { "key": "value"}
# json into dict
empty_dict = dict()
empty_dict = {}

sample_dict = {"a" : 1, "b" : 2, "c" : 3, "d": ["abc", "cba"], "dict2" : {"key1" : "value1"}}
print(sample_dict["dict2"]["key1"])
print(sample_dict["d"][0])

# KeyError: 'key2'
# print(sample_dict["key2"])
print(sample_dict.get("a"))
print(sample_dict.get("key2"))

if sample_dict.get("dict2"):
    print(f"Key was found and value is {sample_dict.get("dict2")}")
else:
    print("Key was not found in dict")

# check for key
print("a" in sample_dict)
# values
print(sample_dict.values())
# check for value
print(1 in sample_dict.values())

# Iteration
for item in sample_dict:
    print(f"Key is {item} and value is {sample_dict[item]}")

print(sample_dict.items())

for k,v in sample_dict.items():
    print(f"Key is {k} and value is {v}")
    print(f"Type of value is: {type(v)}")


d1 = {"key1" : {"a", "b", "c"}}
print(d1)
print(d1["key1"])
print(type(d1["key1"]))

