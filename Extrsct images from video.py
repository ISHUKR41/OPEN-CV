import cv2       
import numpy as np          
cap=cv2.VideoCapture("1video.mp4")
c=0
while True:     
  r,frame=cap.read()
  if r== True:         
    frame=cv2.resize(frame,(500,700))
    filename=r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\capimg\org_img_"+str(c)+".png"
    cv2.imwrite(filename,frame)
    cv2.imshow("video",frame) 
    c=c+1
    if cv2.waitKey(25) & 0xff==ord("p"):
      break
  else:
    break
cap.release()
cv2.destroyAllWindows() 