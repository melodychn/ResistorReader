import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage.filters as sp

# in gray scale img more of one color will look lighter
#[r,g,b]



img = plt.imread("../imgs/r8.jpg")

plt.imshow(img)
plt.show()

img_blur = np.stack((sp.gaussian_filter(img[:,:,0], 5),sp.gaussian_filter(img[:,:,1], 5),sp.gaussian_filter(img[:,:,2], 5)), axis=-1)

green_filter = (img_blur[:,:,1] > 0) * (img_blur[:,:,0] < 100) * (img_blur[:,:,2] < 100)

coords = np.argwhere(green_filter)

max_x = np.max(coords[:,0])
max_y = np.max(coords[:,1])
min_x = np.max(coords[:,0])
min_y = np.max(coords[:,1])

box = [[]]

plt.imshow(green_filter)
plt.show()

#red_filter = (img[:,:,1] > 0) * (img[:,:,0] < 100) * (img[:,:,2] < 100)
#plt.imshow(red_filter)
#plt.show()

#blue_filter = (img[:,:,1] > 0) * (img[:,:,0] < 100) * (img[:,:,2] < 100)
#plt.imshow(blue_filter)
#plt.show()







