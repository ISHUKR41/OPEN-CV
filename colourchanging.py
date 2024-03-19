import cv2 
import numpy as np                  


org=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\9.jpg")
org=cv2.resize(org,(500,700))
new=cv2.cvtColor(org,cv2.COLOR_BGRA2GRAY)
cv2.imshow("org",org)
cv2.imshow("new",new)
cv2.waitKey(0)
cv2.destroyAllWindows()