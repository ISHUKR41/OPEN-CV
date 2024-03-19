import cv2
import numpy as np                         
import os

# cv2.BORDER_CONSTANT:--> it adds constant colored border. The value should be given as a keyword argument 

# cv2.BORDER_REFLECT:--> The border will be mirror reflection of the border elements. 

# cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT:--> it does the same work as cv2.BORDER_REFLECT but with slight changes

# cv2.BORDER_REPLICATE:--> it replicates the last elements 






print("BORDER_CONSTANT:-->")
print()
org_img=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\9.jpg")
res_image=cv2.resize(org_img,(500,500))

img1=cv2.copyMakeBorder(res_image,20,20,20,20,cv2.BORDER_CONSTANT,None,value=2)
img1=cv2.resize(img1,(500,500))
h=np.hstack((res_image,img1))
cv2.imshow("ishu",h)
# print(img.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("BORDER_DEFAULT:-->")

org_img=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\9.jpg")
res_image=cv2.resize(org_img,(500,500))

img2=cv2.copyMakeBorder(res_image,20,20,20,20,cv2.BORDER_DEFAULT,None,value=2)
img2=cv2.resize(img2,(500,500))
h=np.hstack((res_image,img1,img2))
cv2.imshow("ishu",h)
# print(img.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
print()


print("BORDER_REFLECT:-->")
org_img=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\9.jpg")
res_image=cv2.resize(org_img,(500,500))

img3=cv2.copyMakeBorder(res_image,20,20,20,20,cv2.BORDER_REFLECT,None,value=2)
img3=cv2.resize(img1,(500,500))
h=np.hstack((res_image,img1,img2,img3))
cv2.imshow("ishu",h)
# print(img.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()

# IN the border chapter there are many border but approx all symentic are same 

