'''
Created on 2019. febr. 8.

@author: z003vt7v
'''

students = []

"""
__init__ is the constructor method
This way we pass the name and student_id instantly as parameters for the class instance

"""

class Student:
    def __init__(self, name, student_id = 324):
        student = {"name": name, "student_id": student_id}
        students.append(student)
    
    def __str__(self):
        return "Student"


mark = Student("Mark")

print(mark)
print(students)