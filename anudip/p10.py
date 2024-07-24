from tabulate import tabulate
headers = ["stdid","stdname","standard", "Age", "Hindi","English","Maths","Science","Computer","Total"]
students = [
    ["std101","Ashish Kumar"  ,"10th",15,67,89,87,89,90,422],
    ["std102","Abhishek Kumar","10th",14,85,45,48,89,90,422],
    ["std103","Aman"          ,"10th",15,23,56,78,89,90,422],
    ["std104","Rahul"         ,"10th",14,45,67,90,89,90,422],
    ["std105","Ruby"          ,"10th",13,89,67,94,89,90,422],
    ["std106","Suman"         ,"10th",13,90,46,53,89,90,422],
    ["std107","Saurabh"       ,"10th",15,45,23,57,89,90,422],
    ["std108","Sumit"         ,"10th",14,23,45,87,89,90,422],
    ["std109","Kamlesh"       ,"10th",15,45,56,89,89,90,422],
    ["std110","Rohan"         ,"10th",15,34,12,20,89,90,422],
]
#table = [[student[header] for header in headers] for student in students]

print(tabulate(students, headers, tablefmt="grid"))
#students with more than 50 marks in english
print("------------------------------------------------------students with more than 50 marks in english------------------------------------------------")
grade_students = [student[1] for student in students if student[5] >= 50]
print(grade_students)

sorted_students_by_math = sorted(students, key=lambda x: x[6], reverse=True)

# Retrieve the top 4 students in Math
top_4_students_in_math = sorted_students_by_math[:4]

# Print the top 4 students in Math
print("---------------------------------------------------------------Top 4 students in Math:-----------------------------------------------------------")
print(tabulate(top_4_students_in_math,headers, tablefmt="grid"))
