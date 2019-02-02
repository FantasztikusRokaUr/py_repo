'''
Created on Feb 2, 2019

@author: mrfox
'''

names = ["Fox", "Fuchs", "Renard", "Volpe"]

#for works like foreach in other languages
for name in names:
    print(f"My name is {name}.")

print()

x = 0
for index in range(0, 10, 4):
    x += 10
    print("The value of X is {0}".format(x))

print()

for y in range(5, 10):
    print(y)

