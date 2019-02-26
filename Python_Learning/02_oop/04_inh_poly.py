'''
Created on 2019. febr. 8.

@author: z003vt7v
'''

students = []

"""
When you have to classes defined, you can kind of tie them together.
For this example: We want to add a high school student.
So we want every method in the Student class, and attributes, except for a few changes.
So we can create a HighSchoolStudent class and it will inherit from the Student class.
 
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


"""
Within the class body we can override the methods, class attributes, instance attributes.
We can also add new ones.
This class doesn't have the get_name_capitalized method defined, BUT it's parent class does.
We can also override the methods. (get_school_name)
We can override the method, but use the parent classes method with the "super" keyword.
For example we want to have the get_name_capitalized class from the parent class to work, BUT
we want to alter it a little bit.
Here, let's change it, so it will add a -HS (for high school) after the name.
"""
class HighSchoolStudent(Student):
    
    school_name = "Fuchs High School"
    
    def get_school_name(self):
        return "This is a High School Student."
    
    def get_name_capitalized(self):
        original_value = super().get_name_capitalized()
        return original_value + "-HS"

james = HighSchoolStudent("james")

print(james.get_name_capitalized())
print(james.get_school_name())






