import cv2 
import numpy as np            

def wscube(x):
  pass


img=np.zeros((500,500,3),np.unit8)*255
cv2.namedWindow("color_bar")
cv2.createTrackbar("on","color_bar",0,100,wscube)

while True:          
  cv2.imshow("color_bar",img)
  if cv2.waitKey(1) & 0xff==ord("p"):
      break
  on=cv2.getTrackbarPos("on","color_bar")
  img[:]=[0,0,on]
cv2.destroyAllWindows()
