# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 00:35:26 2019

@author: lolly
"""

CONST_BLACK = 0 
CONST_BROWN = 1 
CONST_RED = 2 
CONST_ORANGE = 3 
CONST_YELLOW = 4 
CONST_GREEN = 5 
CONST_BLUE = 6 
CONST_VIOLET = 7 
CONST_GRAY = 8 
CONST_WHITE = 9 
CONST_SILVER = 10 
CONST_GOLD = 11 
 
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.colors as colors 
import scipy.ndimage.filters as sp 
import scipy.signal as sig 
import scipy.spatial.distance as similarity 

def crop (name): 
    img = plt.imread(name) 
     
    plt.imshow(img) 
    plt.show() 
 
    batchWidth = 8 
 
    (h, w) = img.shape[:2] 
    w2 = int(np.ceil(w / float(batchWidth))) 
 
    mods = w % batchWidth 
    if mods == 0: 
        pw = (0, 0) 
    else: 
        pw = (0, batchWidth - mods) 
 
    img = np.stack((np.pad(img[:,:,0], ((0,h), pw), 'symmetric'),np.pad(img[:,:,1], ((0,h), pw), 'symmetric'),np.pad(img[:,:,2], ((0,h), pw), 'symmetric')), axis=-1) 
 
 
    averaged_vals = np.zeros([1,w2,3]) 
    for i in range(w2): 
        r = np.mean(img[:, i * batchWidth:(i + 1) * batchWidth, 0]) 
        b = np.mean(img[:, i * batchWidth:(i + 1) * batchWidth, 1]) 
        g = np.mean(img[:, i * batchWidth:(i + 1) * batchWidth, 2]) 
 
        averaged_vals[0][i][0] = r 
        averaged_vals[0][i][1] = b 
        averaged_vals[0][i][2] = g 
        
    averaged_vals = np.stack((averaged_vals[0],averaged_vals[0],averaged_vals[0],averaged_vals[0],averaged_vals[0],averaged_vals[0]), axis=0) 
    plt.imshow(averaged_vals.astype(int)) 
    plt.show() 
    
    return averaged_vals 

def showColor (array, color): 
      
     def black(): 
         black_filter = (array[:,:,0] < 65) * (array[:,:,1] < 65) * (array[:,:,2] < 65) 
         plt.imshow(black_filter) 
         plt.show() 
         print(color) 
     def brown(): 
         brown_filter = (array[:,:,0] > 50) * (array[:,:,1] < 100) * (array[:,:,2] < 50) 
         plt.imshow(brown_filter)  
         plt.show() 
         print(color) 
     def red(): 
         red_filter = (array[:,:,0] > 170) * (array[:,:,1] < 100) * (array[:,:,2] < 100) 
         plt.imshow(red_filter) 
         plt.show() 
         print(color) 
     def orange(): 
         orange_filter = (array[:,:,0] > 170) * (array[:,:,1] > 70) * (array[:,:,1] < 150)* (array[:,:,2] < 100) 
         plt.imshow(orange_filter) 
         plt.show() 
         print(color) 
     def yellow(): 
         yellow_filter = (array[:,:,0] > 130) * (array[:,:,1] > 130) * (array[:,:,2] < 80) 
         plt.imshow(yellow_filter) 
         plt.show() 
         print(color) 
     def green(): 
         green_filter = (array[:,:,0] < 120) * (array[:,:,1] > 90) * (array[:,:,2] < 120) 
         plt.imshow(green_filter) 
         plt.show() 
         print(color) 
     def blue(): 
         blue_filter = (array[:,:,0] < 80) * (array[:,:,1] < 150) * (array[:,:,2] > 100) 
         plt.imshow(blue_filter) 
         plt.show() 
         print(color) 
     def violet(): 
         violet_filter = (array[:,:,0] > 50) * (array[:,:,1] < 150) * (array[:,:,2] > 140) 
         plt.imshow(violet_filter) 
         plt.show() 
         print(color) 
     def gray(): 
         gray_filter = (array[:,:,0] > 50) * (array[:,:,0] < 200) * (array[:,:,1] > 50) * (array[:,:,1] < 200) * (array[:,:,2] > 50) * (array[:,:,2] < 200) 
         plt.imshow(gray_filter) 
         plt.show() 
         print(color) 
     def white(): 
         white_filter = (array[:,:,0] > 200) * (array[:,:,1] > 200) * (array[:,:,2] > 200) 
         plt.imshow(white_filter) 
         plt.show() 
         print(color) 
         
     filters = {  0: black, 
                 1: brown, 
                 2: red, 
                 3: orange, 
                 4: yellow, 
                 5: green, 
                 6: blue, 
                 7: violet, 
                 8: gray, 
                 9: white, 
                 #10: silver, 
                 #11: gold, 
             } 
 
     filters[color] ()  
   
# Four-band resistors  
          
for x in range (1,11): 
    pic = "./imgs/r" + str(x) + ".jpg" 
    print("r" + str(x)) 
    array = crop(pic) 
     
    for y in range (0,10): 
        showColor(array,y) 
         