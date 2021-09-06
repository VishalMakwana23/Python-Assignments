'''Consider a NumPy array where each row represents data of a student and
there are 10 such rows. The data of a student consists of rollno, name, city
and age. i.e. each row contains rollno, name, city and age of a student. Write
a Python program to find the following:
• Maximum, Minimum and Average age of all the students
• Maximum, Minimum and Average age of all the students living in a
particular city (take input of name of a city from the user)
• Maximum, Minimum and Average age of all the students whose
name starts with the letter ‘A’
• Maximum, Minimum and Average age of all the students having
rollno > n (take input of n from the user)'''





import numpy as np
student = np.array([[15,"hardik","surat",22],
 [54,"ram","rajkot",30],
 [5,"Arm","bhavnager",15],
 [2,"Asham","surat",25],
 [50,"rm","bhavnager",23],
 [24,"sham","surat",22]
 ])
print(student)
age = []
def agedataprint(data):
 print("Fount Data is :- ",data)
 print("Min age is :- ",min(data))
 print("Max age is :- ",max(data))
 print("AVG age is :- ",sum(data)/len(data))
for k,i in enumerate(student):
 age.append(int(student[k][3]))
 
print("---------All The students----------")
agedataprint(age)

city=str(input("Enter the City Name :-"))
age = []
for k,i in enumerate(student):
 if (student[k][2] == city):
     age.append(int(student[k][3]))
     
print("---------City wise students Age Data----------")
agedataprint(age)
name = []
for k,i in enumerate(student):
 if (student[k][1].startswith('A')):
     name.append(int(student[k][3]))


print("---------Name wise strating A students Age Data----------")
agedataprint(name)


n=int(input("Enter the Roll No :-"))
age = []
for k,i in enumerate(student):
 if (int(student[k][0]) > n):
     age.append(int(student[k][3]))

     
print("---------RollNo wise students Age Data----------")
agedataprint(age)
