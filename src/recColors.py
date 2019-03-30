import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import scipy.ndimage.filters as sp
import scipy.signal as sig
import scipy.spatial.distance as similarity

# in gray scale img more of one color will look lighter
#[r,g,b]



img = plt.imread("../imgs/r5.jpg")

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












# imgR = img[:,:,0]
# imgB = img[:,:,1]
# imgG = img[:,:,2]
#
# avg_color1 = np.array([[[int(np.mean(imgR)),int(np.mean(imgB)),int(np.mean(imgG))],[0,0,0],[255,255,255]]])
#
# plt.imshow(avg_color1)
# plt.show()
#
# avg_color = np.array([int(np.mean(imgR)),int(np.mean(imgB)),int(np.mean(imgG))])
#
# img_similarity = np.zeros(imgR.shape)
# for r in range(imgR.shape[0]):
#     for c in range(imgR.shape[1]):
#         img_similarity[r][c] = similarity.euclidean(avg_color, img_blur[r][c]+1e-16)
#
#
#
# #imgR = (imgR > (avg_color[0]+30)) + (imgR < (avg_color[0]-30))
# #imgB = (imgB > (avg_color[0]+30)) + (imgB < (avg_color[0]-30))
# #imgG = (imgG > (avg_color[0]+30)) + (imgG < (avg_color[0]-30))
#
#
# plt.imshow(img_similarity, cmap=plt.cm.gray)
# plt.show()









# img_hsv = colors.rgb_to_hsv(np.stack(((img[:,:,0]/255),(img[:,:,1]/255),(img[:,:,2]/255)), axis=-1))
#
# imgR = img[:,:,0]
# imgB = img[:,:,1]
# imgG = img[:,:,2]
#
# imgH = img_hsv[:,:,0]
# imgS = img_hsv[:,:,1]
# imgV = img_hsv[:,:,2]
#
# kern = np.array([[-1,1]])
#
# imgR = sig.convolve2d(imgR, kern)
# imgG = sig.convolve2d(imgG, kern)
# imgB = sig.convolve2d(imgB, kern)
#
# imgH = sig.convolve2d(imgH, kern)
# imgS = sig.convolve2d(imgS, kern)
# imgV = sig.convolve2d(imgV, kern)
#
# imgedg = (imgR + imgB+ imgG + imgH + imgS + imgV)/6
#
# plt.imshow(imgedg, cmap=plt.cm.gray)
# plt.show()
#
# plt.imshow(imgR, cmap=plt.cm.gray)
# plt.show()
#
# plt.imshow(imgB, cmap=plt.cm.gray)
# plt.show()
#
# plt.imshow(imgG, cmap=plt.cm.gray)
# plt.show()











#img_blur = np.stack(((img[:,:,0]/255),(img[:,:,1]/255),(img[:,:,2]/255)), axis=-1)

#img_hsv = colors.rgb_to_hsv(img_blur)

#green_filter = (img_blur[:,:,1] > 0) * (img_blur[:,:,0] < 100) * (img_blur[:,:,2] < 100)





#plt.imshow(img[:,:,0], cmap=plt.cm.gray)
#plt.show()

#plt.imshow(img[:,:,1], cmap=plt.cm.gray)
#plt.show()

#plt.imshow(img[:,:,2], cmap=plt.cm.gray)
#plt.show()

#plt.imshow(img_hsv[:, :, 0], cmap=plt.cm.gray)
#plt.show()

#plt.imshow(img_hsv[:, :, 1], cmap=plt.cm.gray)
#plt.show()

#plt.imshow(img_hsv[:, :, 2], cmap=plt.cm.gray)
#plt.show()













#bands = np.zeros(green_filter.shape[1])
#for col in range(green_filter.shape[1]):
#    if np.any(green_filter[:,col]):
#        bands[col] = 1

#np.argwhere(bands)



#coords = np.argwhere(green_filter)

#max_x = np.max(coords[:,0])
#max_y = np.max(coords[:,1])
#min_x = np.min(coords[:,0])
#min_y = np.min(coords[:,1])

# score for determining if this is a band width/height so smaller generally better
#band_score = (max_x - min_x)/(max_y - min_y)

#print("band score: ", band_score)

############################################################

#red_filter = (img[:,:,1] > 0) * (img[:,:,0] < 100) * (img[:,:,2] < 100)
#plt.imshow(red_filter)
#plt.show()

#blue_filter = (img[:,:,1] > 0) * (img[:,:,0] < 100) * (img[:,:,2] < 100)
#plt.imshow(blue_filter)
#plt.show()







