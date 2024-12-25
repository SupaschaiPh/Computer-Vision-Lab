import cv2
import numpy as np
img = cv2.imread('./images/balloons.jpeg')

img2 = img.copy()
balloon = img[5:115, 115:200]
img2[15:125, 230:315] = balloon
img2[0:110, 350:435] = balloon
img2[30:140, 500:585] =  balloon


balloon2 = img[156:484, 192:512]
print(balloon.shape ,balloon2.shape)
img2[215:163:, 254:194] =  balloon2


cv2.imshow("img",img2)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
