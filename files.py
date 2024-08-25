from lib2to3.fixes.fix_input import context
from time import sleep
from types import NoneType
import os

file = open('sample.txt', 'r+')
# read line by line
for line in file:
    print(line, end='')
    # if condition

# read lines into the list
lines = file.readlines()
file.close()


# Writing to a file
# file = open('sample.txt', 'w')
# file.writelines(["\nFirst line written\n", "Second line written\n"])
# file.close()

with open('sample.txt', 'r+') as file:
    content = file.readlines()
    print(content)



def read_file_as_list(filename):
    with open(filename, 'r') as file:
        return file.readlines()


file_line = read_file_as_list('sample.txt')
print(file_line)

a = ["a", "b"]
# Exception handling in python
# try:
#     print(a[3])
# except IndexError:
#     print("IndexError happened")
# except:
#     print("Error, but no an IndexError")


try:
    with open('sample1.txt','r') as file:
        content = file.read()
        print("File found")

except FileNotFoundError:
    with open('sample1.txt','w+') as file:
        file.writelines(["\nFirst line written\n", "Second line written\n"])
