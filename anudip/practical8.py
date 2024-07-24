# show only the values in the form of a list
student_data = {"stdid": 1, "stdname": "Rahul Sharma", "class": 10, "age": 15, "hindi": 85, "english": 78, "maths": 92, "science": 88, "computer": 90}
listvar = student_data.values()
print(listvar)

# pop out a element from the dictonary 
new = student_data.pop("hindi")
print(new)
print(student_data)

# update a dictonary using other dictonaries
s1 = {"stdid": 1, "stdname": "Rahul Sharma", "class": 10, "age": 15, "english": 78, "science": 88}
s2 = {"stdname": "Rahul kumar", "age": 16, "hindi": 85, "english": 78, "maths": 92, "science": 88, "computer": 90}
s1.update(s2)
print(s1)

# find the length of the dictonary 
a = len(student_data)
print(a)