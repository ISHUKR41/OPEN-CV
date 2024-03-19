import cv2 
import numpy as np 

img=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\savejonny.jpg")

img1=cv2.flip(img,1) # according to "y" axis
img2=cv2.flip(img,0) # according to "x" axis
img3=cv2.flip(img,-1) # according to "x,y" axis

img4=cv2.rotate(img,cv2.ROTATE_180) # its rotate the image into 180 degrees

#img5=cv2.transpose(img)
#img=cv2.resize(img,img1,img2,img3,img4,img5,(500,700))

print(img.shape)
print(img1.shape)
print(img2.shape)
print(img3.shape)
print(img4.shape)


h1=np.hstack((img,img1,img2,img3,img4))
#v1=np.vstack((img,img1,img2,img3,img4))

cv2.imshow("image",h1)
cv2.waitKey(0)
cv2.destroyAllWindows()
