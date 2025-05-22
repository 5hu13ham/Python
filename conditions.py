"""
Write an application that defines a variable to store a student's grade, for example 85.
Based on the grade, print out the student's letter grade (A, B, C, D, F).
The rules for grading are as follows:

A - 90 and above
B - 80 to 89
C - 70 to 79
D - 60 to 69
F - 59 and below

"""
stu_grade = 0
stu_grade = float(input('Enter a student\'s grade: '))
if (stu_grade > 100):
    print("Enter grade less than 100.")
elif (stu_grade >= 90 and stu_grade <= 100):
    print("A")
elif(stu_grade >= 80 and stu_grade < 90):
    print("B")
elif(stu_grade >= 70 and stu_grade < 80):
    print("C")
elif(stu_grade >= 60 and stu_grade < 70):
    print("D")
else:
    print("F")