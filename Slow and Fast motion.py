import cv2 
import numpy as np
import os            

cap=cv2.VideoCapture("1video.mp4")
while cap.isOpened():
  rat,frame=cap.read()
  frame=cv2.resize(frame,(500,700))
  if rat==True:  
    
    cv2.imshow("video",frame)
    if cv2.waitKey(25) & 0xff==ord("p"):
      # if u increase the speed of video waitkey value ko decrease karna hoga and vice versa
      # for the normal speed use waitkey 25
      # "0" is the static speed 
      break
  else:
    break
cap.release()
cv2.destroyAllWindows()
