# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero
a=int(input("ENTER A NUMBER: "))
b=int(input("ENTER SECOND NUMBER: "))
try:
    div=a/b
    print(div)
    print("INSIDE TRY AND EXPECT")
except ZeroDivisionError as e:
    print(e)
# Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
try:
    num=int(input("ENTER A NUMBER: "))
except ValueError as v:
    print(v)
#Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
try:
    open("anudip.txt")
except FileNotFoundError as f:
    print(f)
#Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical
try:
    num=int(input("ENTER A NUMBER: "))
    num2=int(input("ENTER ANOTHER NUMBER: "))
except:
    print("Both inputs should be numbers")