'''
Created on Feb 9, 2019

@author: mrfox
'''

students = []

class Student:
    '''
    classdocs
    '''
    school_name = "Fox school"

    def __init__(self, name, student_id = 123):
        '''
        Constructor
        '''
        self.name = name
        self.student_id = student_id
        students.append(self)
    
    def __str__(self):
        return "Student " + self.name
    
    def get_name_capitalized(self):
        return self.name.capitalized()
    
    def get_school_name(self):
        return self.school_name()