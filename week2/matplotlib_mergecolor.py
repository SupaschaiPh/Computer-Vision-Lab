import cv2 , os
import matplotlib.pyplot as plt
path = './images/5555.jpg'
img = cv2.imread(path)
b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])

#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([])

plt.subplot(121);plt.imshow(img) # expects distorted color
plt.subplot(122);plt.imshow(img2) # expect true color
#plt.subplot(123);plt.imshow(img3) # expect true color

plt.show()
cv2.imshow('bgr image',img) # expects true color
cv2.imshow('rgb image',img2) # expects distorted color
#cv2.waitKey(0)
cv2.destroyAllWindows()
