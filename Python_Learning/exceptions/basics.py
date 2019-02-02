'''
Created on Feb 2, 2019

@author: mrfox
'''

student = {
    "name": "Fox",
    "address": "Forest",
    "hobbies": "Night Life"
}

try:
    last_name = student["last_name"]
except KeyError:
    print("Error finding key: last_name")

print("This code executes")
print()

student["last_name"] = "Rocky"

try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("Error finding key: last_name")
#except TypeError:
#    print("Sorry mate, can't add these two")
#Universal exception handling
except Exception as e:
    print(e)
    

print("This code executes")
