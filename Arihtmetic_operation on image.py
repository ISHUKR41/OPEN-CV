import cv2
import numpy as np                         
import os

img1=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\8.jpg")
img2=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\9.jpg")
img1=cv2.resize(img1,(500,700))
img2=cv2.resize(img2,(500,700))

new_img=cv2.addWeighted(img1,0.7,img2,1,1)
cv2.imshow("ishu",new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

