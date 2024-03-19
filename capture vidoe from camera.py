import cv2
import numpy as np                         
import os

cap=cv2.VideoCapture(0)
# "0" means it open the internal camera and for external camera we use the "1"

while True:
  # it is use for lopping the camera 
  r,frame=cap.read()
  if r==True:  
    frame=cv2.resize(frame,(500,700))
    cv2.imshow("Camera",frame)
    if cv2.waitKey(25) & 0xff==ord("p"):
      # when we press "p" we get out from the window
      break
  else:
    break
cap.release()
cv2.destroyAllWindows()