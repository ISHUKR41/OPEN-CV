import cv2
import numpy as np                    
import os

img=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\1.jpg",0)
print(img)# it show the bgr (0-255,0-255,0-255)
print()

print("image shape:\n")
print(img.shape)

print()


print("image Resize:\n")
img=cv2.resize(img,(500,700))
print()

print("image showing:\n")
cv2.imshow("Hardcore_study",img) # first mai window name the jisko print karbna hia usko likha jata hai 


cv2.waitKey(0)  # it means huma kitna mili second ka time chaiye when we enter '0' in the waitkey then we press any key

cv2.destroyAllWindows # it destory all the windwo



print("Imread function:\n")
# Imread function

# cv2.IMREAD_COLOR :--> it specifies to load a color image.any transparency of image will be neglected. it is the default falg. Alternatively, wer can pass integer value 1 for this flag. 

# cv2.IMREAD_GRAYSCALE :--> it specifies to laod an image in grayscale mode. Alternatively ,we can pass integer value 0 for this flag. 

# cv2.IMREAD_UNCHANGED :--> it specifies to load an image as    including alpha chanel. Alternatively we can pass interger  value '-1' for this flag

