# Write a program to count the occurance of word "INDIA" in a text file India.txt.

file=open("India.txt","w")
file.write("India is my country. India is in asia. India share good relation with almost all major superpowers.")
file.close()
file=open("India.txt",'r')
c=file.read()
words=c.split()
count1=0
for i in words:
    if(i=="India"):
        count1+=1
print(count1)
file.close()

# Write a program to count and display the lines starting with "T" in a text file story.txt
file = open("story.txt", 'w')
file.write("Clouds drifted lazily across the sky, obscuring the moon's glow.\n")
file.write("The sun set over the horizon, painting the sky with hues of orange and pink.\n")
file.write("Beneath the stars, a quiet serenity embraced the night.\n")
file.write("Tiny droplets of rain began to fall, tapping softly on the windowpane.\n")
file.write("Time seemed to stand still as the world was enveloped in the tranquility of twilight.\n")
file.write("Thunder rumbled in the distance, heralding the arrival of a summer storm.\n")
file.close()

# Open the file in read mode
file = open("story.txt", 'r')

# Read the content of the file
count = 0
content = file.readlines()

# Iterate over each line in the file content
for line in content:
    if line[0] == 'T':
        count += 1

print("Number of lines starting with 'T':", count)
file.close()
#Write a program to count the number of vowels and consonants in a file "Myfile.txt"
file=open("Myfile.txt",'w')
file.write("Time seemed to stand still as the world was enveloped in the tranquility of twilight. \n")
file.close()
file=open("Myfile.txt",'r')
v=file.read()
vowels="aeiouAEIOU"
vow=0
con=0
for i in v:
    if i in vowels:
        vow+=1
    elif i.isalpha() and i not in vowels :
        con+=1
print("Vowels=",vow,"Consonants=",con)
file.close()
#Write a program to count and display number of words starting with "I" in a file "Word.txt"
file=open("Word.txt",'w')
file.write("The Ice Cream Independance. \n")
file.close()
file=open("Word.txt",'r')
I=file.read()
count=0
for i in I:
    if i=="i" or i=="I":
        count+=1
print(count)
#Write a program to display the lines having more than five words in a text file "Notes.txt"
file=open("Notes.txt",'w')
file.write("The Ice Cream Independance Every Child Dream . \n")
file.close()
file=open("Notes.txt",'r')
F=file.read()
word=F.split()
count=0
five=0
for i in word:
    if len(i)==5:
        five+=1
print("five words in a text file",five)
# WAP to create a binary file "stu.dat" and enter students roll number name and marks till user wants
import pickle
file=open("Stu.dat","wb")

while True:
    roll_number = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))
                
    student = {
        'roll_number': roll_number,
        'name': name,
        'marks': marks
        }
            
            # Serialize the student dictionary and write it to the binary file
    pickle.dump(student, file)
            
    more = input("Do you want to enter another record? (yes/no): ").strip().lower()
    if more != 'yes':
        break
file.close()


#write a program to read a binary file storage display the record of student having marks greater than 81
fil=open("Stu.dat","rb")
while True:
    student = pickle.load(fil)
    if student['marks'] > 81:
        print(f"Roll Number: {student['roll_number']}, Name: {student['name']}, Marks: {student['marks']}")
    break
       
fil.close()
        
