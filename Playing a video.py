import cv2
import numpy as np                         
import os



cap=cv2.VideoCapture("1video.mp4")
while cap.isOpened():
  r,frame=cap.read()
  if r==True:  
    frame=cv2.resize(frame,(600,800))
    cv2.imshow("ishu",frame)
    if cv2.waitKey(25) & 0xff==ord("p"):
      break
        
  else:
    break
  
cap.release()
cv2.destroyAllWindows()