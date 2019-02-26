'''
Created on 2019. febr. 8.

The big magic: They are JUST functions. Anonymous functions, but functions.
They don't have a function name, or the def keyword to be defined.
Short 1 line of code that don't take arguments.

In this example:
We have a number and we want to double it.
Easy, right?

def double(x):
    return x * 2

But with lambda...

@author: z003vt7v
'''

double = lambda x: x * 2

"""
We have x as argument and 1 line of function-body
And we call both of them the same way...
"""

print(double(5))

"""
So without overthinking.... 
Lambda functions are simple one line functions to save some space and time sometimes.

So when are they useful?
In higher-order functions, which are regular functions in Python that take another function as their argument.
For example for a filtering algorithm we have to tell a function as argument.
"""