# creating data table using dictonary 
from tabulate import tabulate
students = [
    {"stdid": 1, "stdname": "Rahul Sharma", "class": 10, "age": 15, "hindi": 85, "english": 78, "maths": 92, "science": 88, "computer": 90},
    {"stdid": 2, "stdname": "Anjali Verma", "class": 10, "age": 16, "hindi": 80, "english": 82, "maths": 95, "science": 91, "computer": 89},
    {"stdid": 3, "stdname": "Rohan Mehta", "class": 10, "age": 15, "hindi": 75, "english": 80, "maths": 88, "science": 85, "computer": 87},
    {"stdid": 4, "stdname": "Neha Singh", "class": 10, "age": 16, "hindi": 90, "english": 88, "maths": 94, "science": 92, "computer": 93},
    {"stdid": 5, "stdname": "Amit Patel", "class": 10, "age": 15, "hindi": 78, "english": 75, "maths": 85, "science": 80, "computer": 82},
    {"stdid": 6, "stdname": "Priya Sinha", "class": 10, "age": 16, "hindi": 88, "english": 84, "maths": 89, "science": 87, "computer": 90},
    {"stdid": 7, "stdname": "Suresh Kumar", "class": 10, "age": 15, "hindi": 82, "english": 79, "maths": 90, "science": 86, "computer": 88},
    {"stdid": 8, "stdname": "Rita Desai", "class": 10, "age": 16, "hindi": 85, "english": 83, "maths": 92, "science": 89, "computer": 91},
    {"stdid": 9, "stdname": "Vikram Joshi", "class": 10, "age": 15, "hindi": 77, "english": 76, "maths": 84, "science": 81, "computer": 83},
    {"stdid": 10, "stdname": "Sneha Reddy", "class": 10, "age": 16, "hindi": 89, "english": 85, "maths": 91, "science": 90, "computer": 92},
    {"stdid": 11, "stdname": "Ravi Gupta", "class": 10, "age": 15, "hindi": 80, "english": 78, "maths": 86, "science": 84, "computer": 85},
    {"stdid": 12, "stdname": "Sunita Malhotra", "class": 10, "age": 16, "hindi": 87, "english": 82, "maths": 90, "science": 88, "computer": 89}
]

headers = ["stdid", "stdname", "class", "age", "hindi", "english", "maths", "science", "computer"]
table = [[student[header] for header in headers] for student in students]

print(tabulate(table, headers, tablefmt="grid"))


#students with more than 50 marks in english
print("------------------------------------------------------students with more than 50 marks in english------------------------------------------------")
grade_students = [student['stdname'] for student in students if student['english'] >= 50]
print(tabulate(grade_students, headers[1], tablefmt="grid"))



#sorting on the basis of Maths
sorted_students_by_math = sorted(students, key=lambda x: x['maths'], reverse=True)
# Retrieve the top 4 students in Math
top_4_students_in_math = sorted_students_by_math[:4]
# Print the top 4 students in Math
print("---------------------------------------------------------------Top 4 students in Math:-----------------------------------------------------------")
table1 =  [{student['stdname'],student['age']} for student in top_4_students_in_math]
print(tabulate(table1, headers[:1], tablefmt="grid"))





#sorting on the basis of computer
sorted_students_by_com = sorted(students, key=lambda x: x['computer'])
# Retrieve the least 4 students in Computer
least_4_students_in_com = sorted_students_by_com[:4]
print("---------------------------------------------------------------least 4 students in Computers:-----------------------------------------------------------")
table2 = [[student[header] for header in headers] for student in least_4_students_in_com]
print(tabulate(table2, headers, tablefmt="grid"))