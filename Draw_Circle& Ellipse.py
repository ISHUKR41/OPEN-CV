import cv2
import numpy as np                         
import os

print("For circle shape:-")

x=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\8.jpg")
x=cv2.resize(x,(500,700))
y=cv2.circle(img=x,center=(225,220),radius=185,color=(0,0,255),thickness=-1,lineType=16) 

# for fill the full face use "thickness=-1"

cv2.imshow("ishu",y)
cv2.waitKey(0)
cv2.destroyAllWindows()




# For ellipse image
print("For ellipse image:-")
a=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\8.jpg")
a=cv2.resize(a,(500,700))
b=cv2.ellipse(img=a,center=(225,220),axes=(200,250),angle=10,startAngle=0,endAngle=360,color=(0,0,255),thickness=3,lineType=16) 
txt=cv2.putText(b,text="Dani ji",org=(110,220),fontFace=2,fontScale=2,color=(255,100,255),thickness=3,lineType=16,bottomLeftOrigin=False)
# for fill the full face use "thickness=-1"

cv2.imshow("ishu",txt)
cv2.waitKey(0)
cv2.destroyAllWindows()



