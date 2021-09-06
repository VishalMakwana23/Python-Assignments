'''Q.5. Consider the NumPy array used in Q.4. Write a Python program to do the
following:
• Display details of all the students living in a particular city (take
input of name of a city from the user) in appropriate format
• Display details of all the students having age greater than N (take
input of N from the user) in appropriate format'''

import numpy as np
student = np.array([[15,"hardik","surat",22],
 [54,"ram","rajkot",30],
 [5,"Arm","bhavnager",15],
 [2,"Asham","surat",25],
 [50,"rm","bhavnager",23],
 [24,"sham","surat",22]
 ])
print(student)
def display(data):
 for i in data:
     
 print("------------------------")
 print("Student Roll No :- ",i[0])
 print("Student Name :- ",i[1])
 print("Student City :- ",i[2])
 print("Student Age :-",i[3])


print("---------City wise students Data----------")

city=str(input("Enter the City Name :-"))
studdata = []
for i in range(len(student)):
 if (student[i][2] == city):
 studdata.append(student[i])
display(studdata)
print("---------Age wise students Data----------")

name=int(input("Enter the Age :-"))
age = []
for i in range(len(student)):
 if (int(student[i][3]) > name):
 age.append(student[i])
display(age)
