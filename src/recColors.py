import numpy as np
import matplotlib.pyplot as plt

# in gray scale img more of one color will look lighter
#[r,g,b]



img = plt.imread("./imgs/r1.jpg")

green_filter = (img[:,:,1] > 0) * (img[:,:,0] < 100) * (img[:,:,2] < 100)
plt.imshow(green_filter)
plt.show()

red_filter = (img[:,:,1] > 0) * (img[:,:,0] < 100) * (img[:,:,2] < 100)
plt.imshow(red_filter)
plt.show()

blue_filter = (img[:,:,1] > 0) * (img[:,:,0] < 100) * (img[:,:,2] < 100)
plt.imshow(blue_filter)
plt.show()







