'''
Created on 2019. febr. 8.

@author: z003vt7v
'''

students = []

"""
So the self argument is the first in the method
It refers to the instance of the class
This is not an argument to pass, it will be automatic.
This is the way we refer to our class from a class.
So if we want to call add_student from the Student class like in this example,
we will have to write self.add_student(args)

"""

class Student:
    def add_student(self, name, student_id = 324):
        student = {"name": name, "student_id": student_id}
        students.append(student)
        

#When we instantiate we call a constructor method.
student = Student()
student.add_student("Mark")

print(students)