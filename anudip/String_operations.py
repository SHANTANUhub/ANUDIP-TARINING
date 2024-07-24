# String creation
Name="I am Shubham Rajput"
print(Name)
#Slicing operation helps to get substring from the original string.
print("Name[2:4]",Name[2:4])

print("Name[5:9]",Name[5:9])

print("Name[:15]",Name[:15])

print("Name[2:]",Name[2:])

print("Name[:]",Name[:])

print("Name[0:17:3]",Name[0:17:3])

print("Name[::]",Name[::])

print("Name[::-1]",Name[::-1])

#Capitalize method convert first character of string into uppercase without altering the whole string.
str="shubham rajput"
str=str.capitalize()
print(str)
#Center method aligns string to the center by filling paddings left andright of the string.
str1=str.center(25,"*")
print(str1)
#Count method returns the number of substring in specific range.
counts=str.count('a',5,10)
print(counts)
#endswith method returns boolean value by comparing if string ends with specified substring.
isends=str.endswith("t")
print(isends)
#Find returns the index of element of string.
findis=str.find('t')
print(findis)
# isalnum method checks whether the all characters of the string is alphanumeric or not.
alnum=str.isalnum()
print(alnum)
# isalpha method checks whether the all characters of the string is alphabet or not.
alpha=str.isalpha()
print(alpha)
# isnum method checks whether the all characters of the string is numeric or not.
num=str.isnumeric()
print(num)
# islower method checks whether the all characters of the string are lowercase or not.
lower=str.islower()
print(lower)

# isupper method checks whether the all characters of the string are uppercase or not.
upper=str.isupper()
print(upper)

# strip method removes all the trailing character from the string
str2="------Python------"
right=str2.rstrip('-')
print(right)
left=str2.lstrip('-')
print(left)
both=str2.strip('-')
print(both)

#Swapcase it swaps the uppercase character to lowercase character in string and vice versa
swap=str2.swapcase()
print(swap)
