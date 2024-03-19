import cv2          
import numpy as np                        

img=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\9.jpg")
img=cv2.resize(img,(600,700))
print(img.shape)

#cordinate of image
#img[y1:y2,x1:x2] 

crop=img[:300,200:400]


cv2.imshow("img",img)
cv2.imshow("crop",crop)
cv2.waitKey(0)
cv2.destroyAllWindows()