import cv2
import numpy as np                    
import os

img_get=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\1.jpg")
img_get=cv2.resize(img_get,(500,700))

# img=img_get
# text="Sudanshu"
# org=(75,75)
# fontFace=cv2.FONT_HERSHEY_COMPLEXont
# fontScale=3
# color=(0,0,255)
# thickness=3
# lineType=cv2.LINE_8
# bottomLeftOrigin=False

# All put in the putText ()

txt=cv2.putText(img=img_get,
text="Shubham",
org=(200,500),
fontFace=cv2.FONT_HERSHEY_DUPLEX,
fontScale=1,
color=(200,250,200),
thickness=2,
lineType=cv2.LINE_8,
bottomLeftOrigin=False)

cv2.imshow("ishu",img_get)
cv2.waitKey(0)
cv2.destroyAllWindows()

