#Declare a div() function with two parameters. Then call the function and pass two  numbers and display their division.
def div(a,b):
    if(b!=0):
        result=a/b
        print(result)
    else:
        print("ERROR: Division by zero is not allowed")
div(10,2)

#Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number .
def square(a):
    result=a*a
    print(result)
square(5)

#Using max() and min() functions display the maximum and minimum of 5 random numbers
import random

# Generate 5 random numbers
random_numbers = [random.randint(1, 100) for _ in range(5)]
print("Random Numbers:", random_numbers)
max_number = max(random_numbers)
min_number = min(random_numbers)

print("The maximum number is:", max_number)
print("The minimum number is:", min_number)


#Accept a name from the user and display that in lower case using lower() function
name = input("Enter your name: ")
lowercase_name = name.lower()
print("Your name in lowercase:", lowercase_name)


print("--------------------------------------------------------------------------------------------------------------------------------------------")

#Write a Python program to count the occurrences of each word in a given sentence
str = "To change the overall look of your document. To change the look available in the gallery"
words = str.split()
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print(word_counts)



#Write a Python program to remove a newline in Python
Strng = "\nBest \nDeeptech \nPython \nTraining\n"
str = Strng.replace("\n","")
print(str)


# Write a Python program to reverse words in a string
Strng = "Deeptech Python Training"
print(Strng[::-1])


str="python is programming language. python is OOPs based and python is dynamically typed"
counts=str.count('python')
print(counts)

# Write a Python program to count and display the vowels of a given text
str = "Welcome to python Training"
count = 0
lower_str=str.lower()
for i in lower_str:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        count+=1
        print(i,count)
        
#Write a Python program to Count all letters, digits, and special symbols from the given string
Input = "P@#yn26at^&i5ve"
chars = 0
digit=0
symbols=0
for char in Input:
    if char.isalpha():
        chars+=1
    elif char.isdigit():
        digit+=1
    else:
        symbols+=1
print("Chars=",chars,"alpha=",digit,"symbols=",symbols)


#Write a Python program to remove duplicate characters of a given string
Input = "String and String Function"
result = []
words = Input.split()
for word in words:
    if word not in result:
         result.append(word)
print("String after removing duplicate words:", *result)


# Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string
Input = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
upper=0
lower=0
special=0
num=0
for char in Input:
    if char.isupper():
        upper+=1
    elif char.islower():
        lower+=1
    elif char.isnumeric():
        num+=1
    else:
        special+=1
print("UpperCase :",upper,"LowerCase :",lower,"NumberCase :",num,"SpecialCase :",special)


#Write a Python Count vowels in a string
input= "Welcome to Python Assignment"
count = 0
lower_str=input.lower()
for i in lower_str:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        count+=1
print("Total vowels are:",count)