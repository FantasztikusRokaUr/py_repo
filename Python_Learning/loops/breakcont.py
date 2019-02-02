'''
Created on Feb 2, 2019

@author: mrfox
'''

names = ["Fox", "Fuchs", "Renard", "Volpe", "Roka"]

#Break the cycle when we reach Renard
for name in names:
    if name == "Renard":
        print("Found him! " + name)
        break
    print("Currently testing " + name)

print()

#Skip when we find Renard
for name in names:
    if name == "Renard":
        continue
        print("Found him! " + name)
    print("Currently testing " + name)

