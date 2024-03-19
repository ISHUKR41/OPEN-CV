import cv2
import numpy as np                         
import os


org_img=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\9.jpg")
res_image=cv2.resize(org_img,(400,500))
h=np.hstack((res_image,res_image))
v=np.vstack((h,h))

# here how can save the image in folder with the help of "imwrite" function 

cv2.imwrite("new_img.jpg",v)
cv2.imshow("ishu",v)
cv2.waitKey(0)
cv2.destroyAllWindows()