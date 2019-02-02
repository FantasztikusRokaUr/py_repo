'''
Created on Feb 2, 2019

@author: mrfox
'''

#Simple example
x = 0
while x < 3:
    print("Count is at {0}".format(x))
    x += 1

print()

#Break the cycle when we reach 6
num = 3
while True:
    if num == 6:
        break
    print(num)
    num += 1

print()

#Skip the cycle when x equals 6, and break the cycle when x equals 10
x = 4
while True:
    x += 1
    if x == 6:
        continue
    if x == 10:
        break
    print(x)