'''
Created on Feb 2, 2019

@author: mrfox
'''

names = ["Fox", "Fuchs", "Renard"]
print(names[0])
print(names[-1])
print()

#Change Fox to Roka
names[0] = "Roka"
print(names[0])

#Add Volpe to the list
names.append("Volpe")

#Check if Volpe was added
print("Volpe" in names)

#Get the Length of the list
print(len(names))

#We can delete an element
del names[1]
print(names)
print()

print(names[1:-1])
