'''
Created on 2019. febr. 8.

The read_students yield the lines of the file to the student var.
This way we don't need the readlines() function, but have the same effect.

@author: z003vt7v
'''

students = []


def read_file():
    try:
        f = open("students.txt", "r")
        for student in read_students(f):
            students.append(student)
        f.close()
    except Exception:
        print("Could not read file")


def read_students(f):
    for line in f:
        yield line


read_file()
print(students)
