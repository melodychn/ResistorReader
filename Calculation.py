#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 22:41:38 2019

@author: melodychen
"""


class Calculator:
    resist = 0
    def __init__(self, type):
        self.type = type
    def calculate1(self, color1, color2, color3, color4):
        print("calculating")
        resistance = ((color1*10) + color2)*color3
        return resistance
    def calculate2(self, color1, color2, color3, color4, color5):
        resistance = ((color1*100) + (color2*10) + (color3))*color4
        return resistance
    def calculate(self, color1, color2, color3, color4, color5=0):
        if(type==4):
            resist = calculate1(color1,color2,color3,color4)
        else:
            resist = calculate2(color1,color2,color3,color4,color5)
        return resist