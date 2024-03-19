import cv2 
import numpy as np          
import os             

# --> Image pyramid 
#  Work with images with default resolution but many times we need to change the resolution (lower it )
#  or resize the original image in that case image pyramid comes handy 

img=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\8.jpg")
print(img.shape)
img1=cv2.resize(img,(500,700))
cv2.imshow("image",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

print()

img=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\8.jpg")
print(img1.shape)
img1=cv2.resize(img,(500,700))
new=cv2.pyrDown(img1)
print(new.shape)
cv2.imshow("image",new)
cv2.waitKey(0)
cv2.destroyAllWindows()


img=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\8.jpg")
print(img1.shape)
img1=cv2.resize(img,(500,700))
big=cv2.pyrUp(img1)
print(big.shape)
cv2.imshow("image",big)
cv2.waitKey(0)
cv2.destroyAllWindows()