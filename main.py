#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 00:47:34 2019

@author: melodychen
"""
from Calculation import Calculator
#import ImageReader
def detectResistance():
    file = open("image.jpg","r")
    #pass in file into Image Reader
    #get the parameter passed back from Image Reader
    calc = Calculator(4)
    resist = calc.calculate(color1,color2,color3,color4)
    print("Resistance:")
    print(resist)
