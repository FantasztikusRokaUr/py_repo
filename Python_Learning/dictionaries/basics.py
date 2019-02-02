'''
Created on Feb 2, 2019

Dictionaries are made bye key-value pairs

@author: mrfox
'''

student = {
    "name": "Fox",
    "address": "forest",
    "hobbies": "night life"
}
print(student["name"])
print(student["address"])

print()

#Creating a list of dictionaries
students = [
    {"name": "Fox", "address": "forest", "hobbies": "night life"},
    {"name": "Volpe", "address": "forest", "hobbies": "hunting"},
    {"name": "Renard", "address": "forest", "hobbies": "chicken stealing"},
]

for people in students:
    print(people["hobbies"])

print()
#If there is no key, give it a default value:
print(student.get("Last_Name", "Unknown"))

#Get every key:
print(student.keys())
#Get every value:
print(student.values())

#Deleting a key
del student["name"]
print(student.keys())
