'''
Created on 2019. febr. 8.

@author: z003vt7v
'''

students = []

"""
Let's get rid of the dictionary for now
By creating self.name and self.student_id we create INSTANCE attributes
that can be reached of the instance we create from the class.

Now the students list will be a list containing the entire instance of our class.
From now on it will be the list of all student classes with all the methods and attributes it carries.

Other way of setting INSTANCE attributes is by using setters.

CLASS attributes on the other hand are attributes that are set for every single instance.
It is the attribute of the blueprint basically that we want to see in every instance.
They are not defined by a method, they are not tied to self, or the instance.
They. Are. Static.
To define them, write them outside of any method body, but still inside the class body.
In this example: school_name
This can be accessed even without creating an instance.
"""

class Student:
    
    school_name = "Fox Elementary"
    
    def __init__(self, name, student_id = 324):
        self.name = name
        self.student_id = student_id
        students.append(self)
    
    #also let's add self.name to the __str__ special method
    def __str__(self):
        return "Student " + self.name

    def get_name_capitalized(self):
        return self.name.capitalize()
    
    def get_school_name(self):
        return self.school_name

mark = Student("Mark")

print(mark)
print(students)

#Getting the school name of the instance
print(mark.get_school_name())

#Getting the school name without creating instance
print(Student.school_name)







