import cv2
import numpy as np                    
import os

list_name=os.listdir("C:\\Users\\ISHU\\OneDrive\\Desktop\\OPEN CV\\New folder")
list_name

for name in list_name:
  path="C:\\Users\\ISHU\\OneDrive\\Desktop\\OPEN CV\\New folder"
  img_name=path+"\\"+name
  img=cv2.imread(img_name)
  img=cv2.resize(img,(500,700))
  cv2.imshow("Hardcore_study",img)
  cv2.waitKey(3000)
cv2.destroyAllWindows()

  