# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 00:35:26 2019

@author: lolly
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage.filters as sp

for x in range (1,11):
    img = plt.imread("./imgs/r" + str(x) + ".jpg")
    
    img_blur = np.stack((sp.gaussian_filter(img[:,:,0], 5),sp.gaussian_filter(img[:,:,1], 5),sp.gaussian_filter(img[:,:,2], 5)), axis=-1)
    violet_filter = (img_blur[:,:,0] > 50) * (img_blur[:,:,1] < 150) * (img_blur[:,:,2] > 140)
    
    plt.imshow(violet_filter)
    plt.show()

#green_filter = (img_blur[:,:,0] < 120) * (img_blur[:,:,1] > 90) * (img_blur[:,:,2] < 120)
#red_filter = (img_blur[:,:,0] > 170) * (img_blur[:,:,1] < 100) * (img_blur[:,:,2] < 100)
#black_filter = (img_blur[:,:,0] < 65) * (img_blur[:,:,1] < 65) * (img_blur[:,:,2] < 65)
#yellow_filter = (img_blur[:,:,0] > 130) * (img_blur[:,:,1] > 130) * (img_blur[:,:,2] < 80)
#orange_filter = (img_blur[:,:,0] > 170) * (img_blur[:,:,1] > 70) * (img_blur[:,:,1] < 150)* (img_blur[:,:,2] < 100)
#white_filter = (img_blur[:,:,0] > 200) * (img_blur[:,:,1] > 200) * (img_blur[:,:,2] > 200)
#blue_filter = (img_blur[:,:,0] < 80) * (img_blur[:,:,1] < 150) * (img_blur[:,:,2] > 100)