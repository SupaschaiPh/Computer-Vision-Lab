import cv2
import numpy as np
# mouse callback function
r ,g ,b = [255,127,0]

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to circle
ix,iy = -1,-1

def draw_circle(event,x,y,flags,param):
    global r , g, b
    global ix,iy,drawing,mode        
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(r,g,b),-1)
            else:
                cv2.circle(img,(x,y),5,(r,g,b),-1)
                r -= 1
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(r,g,b),-1)
            r -= 1
        else:
            cv2.circle(img,(x,y),5,(r,g,b),-1)
            r -= 1
    


# Create a black image, a window
# and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image') # สร้างหน้าต่างไว้แต่ยังไม่โชว์
cv2.setMouseCallback('image',draw_circle) # ผูก Callback

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1)
    if k == ord('m'):
        mode = not mode
    elif k == 27: # key ESC
        break

cv2.destroyAllWindows()
