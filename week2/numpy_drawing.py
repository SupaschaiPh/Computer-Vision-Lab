import numpy as np
import cv2
# Create a black image
img = np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)

# Draw a green rectangle at the top-right corner of image
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

# Draw a circle inside the rectangle drawn above.
# -1 = Filled
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)

# Drawing Ellipse
# Draws a half ellipse at the center of the image.
# (256,256) = Center point of Ellipse
# 0 = x
# 0 = y
# 180 = Half of Ellipse
# Color = (255, 0, 0) (because img is color)
img = cv2. ellipse(img,(256,256),(100,50),90, 0,180, 255,-1)

# Draw a small polygon of with four vertices in yellow color
# shape ROWSx1x2 row = มุม
# where ROWS are number of vertices, and it should be of type int32
# วาด เหลี่ยม
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
# isClosed ลากเส้นให้ปิด (ลากมาจุดเริ่มต้มด้วย)
img = cv2.polylines(img,[pts],True,(0,255,255))

# Write 'OpenCV' on the image in white color
font = cv2.FONT_HERSHEY_SIMPLEX

text = cv2.putText(img, 'I Love Somkiat', (20,500), font, 2,(255,255,255), 2, cv2.LINE_AA)
cv2.imshow('Drawing on an image',img)

k = cv2.waitKey(0)
