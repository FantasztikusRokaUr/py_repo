'''
Created on 2019. febr. 8.

@author: z003vt7v
'''

def get_students():
    students = ["mark", "james"]
    def get_students_titlecase():
        students_titlecase = []
        for student in students:
            students_titlecase.append(student.title())
        return students_titlecase
    student_titlecase_names = get_students_titlecase()
    print(student_titlecase_names)

get_students()
