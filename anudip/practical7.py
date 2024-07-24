# creating data table using list
import pandas as pd 
from tabulate import tabulate

students = [
    ["sid101", "ashish kumar", "10th", 15, 67, 89, 87, 89, 90, 422],
    ["sid102", "abhishek kumar", "10th", 14, 85, 45, 48, 90, 45, 313],
    ["sid103", "aman", "10th", 15, 23, 56, 78, 78, 67, 302],
    ["sid104", "rahul", "10th", 14, 45, 67, 45, 45, 56, 258],
    ["sid105", "ruby", "10th", 13, 89, 67, 89, 93, 65, 403],
    ["sid106", "suman", "10th", 13, 90, 46, 67, 67, 67, 337],
    ["sid107", "saurabh", "10th", 15, 45, 23, 34, 45, 34, 181],
    ["sid108", "sumit", "10th", 14, 23, 45, 67, 78, 90, 303],
    ["sid109", "kamlesh", "10th", 15, 45, 56, 78, 99, 67, 345],
    ["sid110", "rohan", "10th", 15, 34, 12, 24,45,56,171],
]

# to show the data in column form
col=['stdid','stdname','standard','age','hindi','english','math', 'science', 'computer','total']
df=pd.DataFrame(data=students,columns=col)
print(df)

# to show the data in the form of table using the tabulate library of python
student_tabulate= tabulate(students,headers=col, tablefmt="grid")
print(student_tabulate)

#display the name of students whose marks in english is greather than 50
for row in students:
    if(row[5]>50):
        print(row[1])
print()
        
# display students name and age of top four scorer of maths        
sorts = sorted(students, key=lambda student: student[6] ,reverse=True)
print("name","age")
print(sorts[0][1],sorts[0][3])
print(sorts[1][1],sorts[1][3])
print(sorts[2][1],sorts[2][3])
print(sorts[3][1],sorts[3][3])
print()

# display name id age of student who are bottom three scorer
sorts1 = sorted(students, key=lambda student: student[5])
print("id","name","age")
print(sorts1[0][0],sorts1[0][1],sorts1[0][3])
print(sorts1[1][0],sorts1[1][1],sorts1[1][3])
print(sorts1[2][0],sorts1[2][1],sorts1[2][3])
print(sorts1[3][0],sorts1[3][1],sorts1[3][3])