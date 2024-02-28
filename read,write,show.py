import cv2
import numpy as np
im=cv2.imread("C:\\Users\\Admin\\Pictures\\saved images\\images.png")
cv2.imwrite("C:\\Users\\Admin\\Pictures\\saved images\\images2.png",im)
cv2.imshow("hello",im)
cv2.waitKey(0)  
cv2.destroyAllWindows() 
