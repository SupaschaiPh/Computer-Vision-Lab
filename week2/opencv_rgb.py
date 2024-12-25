import numpy as np
import cv2 , random
while True:
    # Create a black image
    img = np.zeros((512,512,3), np.uint8)

    # Write 'OpenCV' on the image in white color
    font = cv2.FONT_HERSHEY_SIMPLEX

    r,g,b = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    text = cv2.putText(img, 'I Love Somkiat', (20,500), font, 2,(r,g,b), 2, cv2.LINE_AA)
    text = cv2.putText(img, 'I Love Somkiat', (20,50), font, 2,(r,g,b), 2, cv2.LINE_AA)
    text = cv2.putText(img, 'I Love Somkiat', (20,250), font, 2,(r,g,b), 2, cv2.LINE_AA)


    cv2.imshow('Drawing on an image',img)

    k = cv2.waitKey(10)
    if cv2.waitKey(30) == ord('q'):
        break
