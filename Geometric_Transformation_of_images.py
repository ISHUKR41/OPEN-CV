import cv2 
import numpy as np             

# transformation :-
#  1.scaling
#  2.translation 
#  3.Rotation
 
# --> Affline transformation:
#   All parallel lines in the original image will still be parallel in the output image. 

# --> To find the transformation matrix,we need three points from the input image and their corresponding location in the output image. 

# --> Then cv2.getAffine Transform will create a 2*3 matrix which is to be passes to cv.wrapAffine. 

# -->prespective Transformation :
#   you need 3*3 transformationmatrix. straight lines will remain straight even after the transformation. 

# you need 4 points on the input image and corresponding points on the output image. 

# Among these 4 points, 3 of them should not be collinear. 

# then the transformation matrix can be found by the function cv2.getPerspectiveTransform. 

# then apply cv.wrapPerspective with this 3*3 transformation matrix 


#-------Background Subtraction in opencv------


org_v=cv2.VideoCapture("1video.mp4")
sub_m=cv2.createBackgroundSubtractorMOG2()
while True:                
  r,frame=org_v.read()
  if  r== True:               
      frame=cv2.resize(frame,(700,500))
      sub_v=sub_m.apply(frame)
      cv2.imshow("Sub",sub_v)
      cv2.imshow("video",frame)
      if cv2.waitKey(25) & 0xff==ord("p"):
          break
  else:
    break
  org_v.release()
  cv2.destroyAllWindows()
  
  
# --> its output is binary segmented image which essentially gives information about the non-stationary objects in the image.

# --> there lies a problem in the concept of finding non stationary portion as the shadow of the moving and sometimes being classified in the foreground 

