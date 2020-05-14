#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment: CA3
Student ID : 10543531
Student Name: Wenjuan Zhao
Git hub: https://github.com/lulu0066/B8IT105.git

"""

from functools import reduce

  
class myClass:
    # add two lists using lambda and map function
    def addFunc(self,values1,values2):
        return list(map(lambda x,y:x+y,values1,values2))
    # calculating the square of each value in a list
    def squareFunc(self,values):
        return list(map(lambda x:x*x, values))
    # calculating the cube of each value in a list
    def cubeFunc(self,values):
        return list(map(lambda x:x**3, values))
    # find the number that can be divided by 3 using filter function
    def divideBy3Func(self,values):
        return list(filter(lambda x:x%3 ==0, values))
    # find the number that can not be divided by 2 using filter function
    def notDevideBy2Func(self,values):
       return list(filter(lambda x:x%2 !=0, values)) 
    # using reduce function to get the min value
    def minFunc(self,values):
        return reduce(lambda x,y:x if (x < y) else y, values)
    # using reduce function to get the max value
    def maxFunc(self,values):
        return reduce(lambda x,y:x if (x > y) else y, values)
    # calulate the sum of all values in a list
    def sumFunc(self,values): 
        return reduce(lambda x,y:x + y, values)
    # list comprehetion function - multiply by 2
    def multiFunc(self,values): 
        return [(x * 2) for x in values]
    # generator comprehetion
    def genFunc(self,values):
        return list((i for i in values if i % 2 == 0))

result = myClass() 
a = [1, 3, 5, 13, 38, 54, 66]
b = [2, 4, 6, 8, 10, 11, 12]
print(result.addFunc(a,b))
print(result.squareFunc(a))
print(result.cubeFunc(a))
print(result.divideBy3Func(a))
print(result.notDevideBy2Func(b))
print(result.minFunc(a))
print(result.maxFunc(a))
print(result.sumFunc(a))
print(result.multiFunc(b))
print(result.genFunc(a))




    
    