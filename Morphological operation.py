import cv2 
import numpy as np
import os                

# Morphological operation are used to extract image component that are useful in representation and description of region shape 

# it is typically performed on binary images. 


# --> the morphological operation we will be covering include :
#   1.Erosion 
#   2.dilation  
#   3.Opening
#   4.Closing 
#   5.Morphological gradient 
#   6.Black hat
#   7.Top hat(also called "White hat")
  
#  --> Erosion
#  1. It erodes away the boundaries of foreground object(Always try to keep foreground in white). 
#  2.The kernel slides through the image (as in 2D convolution).
#  3.A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1, Otherwise it is eroded (made to zero). 
#  4. Erosion removes white noises 
 
#  --> Dilation 
#  1.A pixel element is "1" if at least one pixel under the kernel is 1. so it increases the white region in the image or size of foreground object increases 
 
#  2. Normally ,in cases like noise removal erosion is followed by dilatin . because ,erosion removes white noises but it also shrinks our objects 
 

# --> Opening 
#  1.Opening is just another name of erosion followed by dilation 
#  2. It is useful in removing noise 
 

#  --> Closing
#  1. Clsoing is reverse of Opening ,Dilation followed by Erosion
#  2.It is useful in closing small holes inside the foreground objects or samll black points on the object. 
 
 
#  --> Morphological Gradints 
#  1. it is hte difference between Dilation and erosion of an image 
 
#  --> Top hat 
#  1. It is the difference between input image and opening of the image 
 
 
# --> Black hat 
# it is the difference between the closing of the input image and input image 

import cv2 
import numpy as np            
import os                        
img=cv2.imread("13.png")
img=cv2.resize(img,(500,700))
img1=cv2.imread("14.png")
img1=cv2.resize(img1,(500,700))



m=np.ones((18,18),np.int8)
print(m)
er=cv2.erode(img,m,iterations=1)
di=cv2.dilate(img,m,iterations=1)
op=cv2.morphologyEx(img,cv2.MORPH_OPEN,m,iterations=1)
cl=cv2.morphologyEx(img1,cv2.MORPH_CLOSE,m,iterations=1)
gr=cv2.morphologyEx(img1,cv2.MORPH_GRADIENT,m,iterations=1)
tp=cv2.morphologyEx(img1,cv2.MORPH_TOPHAT,m,iterations=1)
bt=cv2.morphologyEx(img1,cv2.MORPH_BLACKHAT,m,iterations=1)
h=np.hstack((img,er,di,op,))
h=cv2.resize(h,(1000,700))
h1=np.hstack((img1,cl,gr,tp,bt))
h1=cv2.resize(h1,(1000,700))

print() 
cv2.imshow("img1",h)
cv2.imshow("Closing_img",h1)
cv2.waitKey(0) 
cv2.destroyAllWindows()   
