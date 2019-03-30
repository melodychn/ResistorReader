# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 00:35:26 2019

@author: lolly
"""

import numpy as np
import matplotlib.pyplot as plt

for x in range (1,12):
    #img1 = plt.imread("./imgs/r1.jpg")
    img = plt.imread("./imgs/r" + str(x) + ".jpg")
    red_filter = (img[:,:,0] > 150 ) * (img[:,:,1] < 100) * (img[:,:,2] < 100)
    plt.imshow(red_filter)
    plt.show()

#green_filter = (img[:,:,1] > 0) * (img[:,:,0] < 100) * (img[:,:,2] < 100)
#plt.imshow(green_filter)
#plt.show()

