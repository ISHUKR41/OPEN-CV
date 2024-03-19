import cv2
import numpy as np                         
import os

x=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\8.jpg")
x=cv2.resize(x,(500,700))

y=cv2.polylines(x,pts=[np.array([[95,350],[95,100],[250,50],[400,100],[400,350]])],isClosed=True,color=(255,255,255),thickness=4,lineType=16)

cv2.imshow("ishu",y)
cv2.waitKey(0)
cv2.destroyAllWindows()
