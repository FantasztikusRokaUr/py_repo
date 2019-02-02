'''
Created on Feb 2, 2019

@author: mrfox
'''

#If statement simplest example:

number = 5
if number == 5:
    print("Yap, it is 5")
else:
    print("Nope, it is not 5")

print()

#It's enough if the number istn't 0
if number:
    print("It is not 0")

text = "Text"
if text:
    print("It's not empty")

aliens = None
if aliens:
    print("This won't be shown")

print()

#Using and/or boolean expressions is also an option
if number == 5 and text == "Text":
    print("And is working.")

if number == 5 or aliens:
    print("Or is working.")

print()

#Ternary if statement
print("Smaller") if 5>4 else print("Bigger")



