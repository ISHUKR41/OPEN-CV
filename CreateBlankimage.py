import cv2  
import numpy as np                    

img=cv2.imread(r"C:/Users/ISHU/OneDrive/Desktop/OPEN CV/New folder/9.jpg")
print(img.shape)
print(img)
new_img=np.ones((500,500,3),np.uint8)*255

new_img1=np.zeros((500,500,3),np.uint8)*255
cv2.imshow("new_img",new_img)
cv2.imshow("new_img1",new_img1)
cv2.waitKey(0)
cv2.destroyAllWindows()