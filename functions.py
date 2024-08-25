# def function_name(pam1, pam2, pam3):
#     print(f"Parameter 1: {pam1}\nParameter 2: {pam2}\nParameter 3: {pam3}")
#
# function_name("Hello", "World", "!")
# function_name("a", "b", "c")
from zoneinfo import available_timezones


def avg_of_list(item: list, n: int):
    return round(sum(item) / len(item), n)


a1 = avg_of_list([23, 42, 12, 65, 76], 2)
a2 = avg_of_list([2, 4, 5, 12, 756, 23], 4)


# def double_value(a: int):
#     return a * avg_of_list()


# a = 10.3
# result = double_value(2)
# print(result)


# *args, **kwargs

def greet_people(greeting, *args):
    for name in args:
        print(f"{greeting} {name}")


greet_people("Hello", "Alice", "Bob", "Jakob", "Marcin")


def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"Key: {key}, Value: {value}")


print_user_info(name="Alice", age=35, isFemale=True, city="Warsaw")

def custom_greet(message, *args, **kwargs):
    if args:
        message += " " + " ".join(args)
    if kwargs:
        message += " | " + ", ".join(f"{k}={v}" for k,v in kwargs.items())
    print(message)

custom_greet("Welcome", "Alice", "Bob", title="Dr.", location="Hospital")