# some packages are included in python by default
#     so you do not have to install random now
import random

# string variable
name = "Nina"
# int variable
age = 24

# print variable with text
print(f"\nHi {name}! We are in {__file__} file\n")

# print multi-line string
print("""Today we will generate random integers 
and compare them to each other\n\n""")

# genearet random int and store it in variables
a = random.randint(0,100)
b = random.randint(0,100)

if a > b:
    print(f"a with value {a} is greater then b with value of {b}")
elif a < b:
    print(f"b with value {b} is greater then a with value of {a}")
else:
    print(f"a and b are equal with value {a}")
