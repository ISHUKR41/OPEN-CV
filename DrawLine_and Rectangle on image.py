import cv2
import numpy as np                    
import os

old_img=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\8.jpg")
old_img=cv2.resize(old_img,(1000,1500))


# pt1=position of 1
# pt2=position of 2

new_img=cv2.line(img=old_img,pt1=(500,600),pt2=(600,600),color=(0,255,100),thickness=2,lineType=4)


cv2.imshow("ishu",new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("for rectangle image:-")


a=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\8.jpg")
a=cv2.resize(a,(1000,1500))
b=cv2.rectangle(img=a,pt1=(200,400),pt2=(300,700),color=(0,255,100),thickness=2,lineType=16)
cv2.imshow("ish",b)
cv2.waitKey(0) 
cv2.destroyAllWindows()


 