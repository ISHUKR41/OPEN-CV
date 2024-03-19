import cv2
import numpy as np                         
import os 

img=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\5.jpg")
img=cv2.resize(img,(500,700))
print(img.shape)

# We also use apertureSize in canny module  and also use the L2gradient module

new_img=cv2.Canny(img,75,70)
cv2.imshow("ish",img)
cv2.imshow("ishu",new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
