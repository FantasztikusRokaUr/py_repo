'''
Created on 2019. febr. 7.

@author: mrfox
'''

students = []


#students is a dictionary list not just a simple string list,
#therefore we have to specify the dict key.
def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student["name"].title()
    return students_titlecase


def print_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student["name"].title()
    print(students_titlecase)


def add_student(name, student_id = 324):
    student = {"name": name, "student_id": student_id}
    students.append(student)
    #Here, we have a list of dictionaries


'''
The more elegant way would be this:

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

The get_student function returns the value we want to use.
'''


#Opening a file: "w" writing, "r" reading, "a" appending, "rb" read binary, "wb" write binary.
def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not read file")


def read_file():
    try:
        f = open("student.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")

student_list = get_students_titlecase()

student_name = input("Enter student name:")
student_id = input("Enter student id:")

add_student(student_name, student_id)
print_students_titlecase()