import cv2
import numpy as np                         
import os

print("AND operation")

img1=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\11.jpg")
img2=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\12.jpg")
img1=cv2.resize(img1,(500,700))
img2=cv2.resize(img2,(500,700))
new=cv2.bitwise_and(img1,img2)
h=np.hstack((img1,img2,new))
cv2.imshow("ishu",h)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("OR operation:-")

img1=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\11.jpg")
img2=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\12.jpg")
img1=cv2.resize(img1,(500,700))
img2=cv2.resize(img2,(500,700))
new=cv2.bitwise_or(img1,img2)
h=np.hstack((img1,img2,new))
cv2.imshow("ishu",h)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("XOR operation:-")
img1=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\11.jpg")
img2=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\12.jpg")
img1=cv2.resize(img1,(500,700))
img2=cv2.resize(img2,(500,700))
new=cv2.bitwise_xor(img1,img2)
h=np.hstack((img1,img2,new))
cv2.imshow("ishu",h)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("NOT operation:-")

# Not operation is work only in one image not two images

img1=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\11.jpg")
img2=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\12.jpg")
img1=cv2.resize(img1,(300,400))
img2=cv2.resize(img2,(300,400))
new=cv2.bitwise_not(img1)
new1=cv2.bitwise_not(img2)
h=np.hstack((img1,new))
h1=np.hstack((img2,new1))

v=np.vstack((h,h1))
cv2.imshow("ishu",v)


cv2.waitKey(0)
cv2.destroyAllWindows()


