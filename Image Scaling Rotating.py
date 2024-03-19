import cv2
import numpy as np                         
import os 

img=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\5.jpg")
res_img=cv2.resize(img,(500,700))

cv2.imshow("ish",img)
cv2.imshow("ishu",res_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("Rotation of image:-")
img=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\5.jpg")
res_img=cv2.resize(img,(500,700))
res_img.shape
print(res_img.shape)
w,h=res_img.shape[0],res_img.shape[1]
m=cv2.getRotationMatrix2D((w/2,h/2),40,1)
new_img=cv2.warpAffine(res_img,m,(h,w))
h=np.hstack((res_img,new_img))
cv2.imshow("isu",h)
cv2.waitKey(0)
cv2.destroyAllWindows() 