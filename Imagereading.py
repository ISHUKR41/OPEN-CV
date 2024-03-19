import cv2 
import numpy as np
img=cv2.imread("anand.jpg") #Image read
re_img=cv2.resize(img,(500,700))
cv2.imshow("OPEN CV",re_img) #Image show

cv2.waitKey(0) #Wait for jb tak koi or key press nhi karta hu. 
cv2.destroyAllWindows()
print()


print("Multiple image showing:")

img=cv2.imread("anand.jpg") #Image read
print(img)



img=cv2.imread("anand.jpg") #Image read
re_img=cv2.resize(img,(300,300))
h=np.hstack((re_img,re_img,re_img))
v=np.vstack((h,h))
cv2.imshow("OPEN CV",v) #Image show
cv2.waitKey(0) #Wait for jb tak koi or key press nhi karta hu. 
cv2.destroyAllWindows()
