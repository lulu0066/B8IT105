#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment: CA3
Student ID : 10543531
Student Name: Wenjuan Zhao
Git hub: https://github.com/lulu0066/B8IT105.git

"""

import unittest 
from CA3 import myClass 
a = [2,3,4,6]
b = [12,13,14,15]
class SimpleTest(unittest.TestCase): 
    def setUp(self):
        self.cal3 = myClass()
    # test add function
    def testAdd(self):
        self.assertTrue([14,16,18,21], self.cal3.addFunc(a,b))
    # test square function   
    def testSquare(self):
        self.assertTrue([4,9,16,36], self.cal3.squareFunc(a))
    # test cube function
    def testCube(self):
        self.assertTrue([8,27,64,216], self.cal3.cubeFunc(a))
    # test devide by 3 function
    def testDevidBy3(self):
        self.assertTrue([3,6], self.cal3.divideBy3Func(a))
    # test devide by 3 function
    def testNotDevideBy2(self):
        self.assertTrue([13,15], self.cal3.notDevideBy2Func(b))
    # test min function   
    def testMin(self):
        self.assertTrue([2], self.cal3.minFunc(a))
    # test max function
    def testMax(self):
        self.assertTrue([6], self.cal3.maxFunc(a))
    # test sum function
    def testSum(self):
        self.assertTrue([15], self.cal3.sumFunc(a))
    # test multiply function
    def testMulti(self):
        self.assertTrue([4,6,8,12], self.cal3.multiFunc(a))
    # test generator comprehetion function
    def testGen(self):
        self.assertTrue([2,4,6], self.cal3.genFunc(a))
if __name__ == '__main__': 
    unittest.main() 