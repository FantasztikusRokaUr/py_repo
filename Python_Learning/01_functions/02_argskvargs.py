'''
Created on 2019. febr. 7.

Tuples can be used for *args, and dictionaries for **kwargs

@author: z003vt7v
'''

students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
    return students_titlecase


def print_students_titlecase():
    print(get_students_titlecase())


def add_student(name, student_id = 324):
    student = {"name": name, "student_id": student_id}
    students.append(student)
    #Here, we have a list of dictionaries


#varargs example:
def var_args(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs["description"], kwargs["feedback"])


var_args("Name", 1, 15, description = 2, feedback = "e")

def print_args(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)

print("**********")
print_args(12, 13, 14, 15, 16)

def print_kwargs(red, green, blue, **kwargs):
    print("r = ", red)
    print("g = ", green)
    print("b = ", blue)
    print(kwargs)

print()
print("**************")

k = {'red': 21, 'green': 65, 'blue':120, 'alpha': 52}
print_kwargs(**k)




