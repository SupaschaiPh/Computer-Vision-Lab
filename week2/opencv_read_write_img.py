import cv2 , os 
#print(cv2.__version__)
print(os.getcwd())
img = cv2.imread("./images/5555.jpg",cv2.IMREAD_REDUCED_GRAYSCALE_2)
cv2.imshow('Somkiat',img)
k = cv2.waitKey(0)

# Press any for exit in windows
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("hehehe.jpg",img)
    cv2.destroyAllWindows()





