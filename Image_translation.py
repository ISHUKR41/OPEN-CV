import cv2            
import numpy as np


# Advantage / Application of image translation are:-
#  1.hiding a part of the image
#  2.cropping the image
#  3.shifting an image
#  4.Animating an image using image translation in loop
   
img=cv2.imread("13.png")
img=cv2.resize(img,(500,700))

# create a matrix

m=np.float32([[1,0,100],[0,1,50]])
print(img.shape)
print()
print(m)
print(img)
new=cv2.warpAffine(img,m,(700,500))
cv2.imshow("Pic",img)
cv2.imshow("Pic2",m)
cv2.imshow("pic3",new)
cv2.waitKey(0)
cv2.destroyAllWindows()