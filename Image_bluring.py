import cv2
import numpy as np                         
import os


# gaussian bluring:--> Gaussian blur is the result of bluring an image by a Gaussian function 

# It is a widely used effect in graphic software, Typically to reduce image noise and reduce detail. 

# it is also used as a preprocessing stage before applying our machine learning or deep learning models. 



# Median Blur:--> The median filter is a non-linear digital filtering techinque, often used to remove noise from image or signal. 

# Median Filtering is very widely used in digital image processing because, under certain conditions,it preserves edges while removing noise. 

# It is one of the best algorithms to remove Salt and paper noise. 





# Bilateral Blur:--> A bilteral filter is a non-linear, edge-preserving and noise-reducing smoothing filter for images. 

# It replaces the intensity of each pixel with a weighted average of intensity values from nearby pixels. 

# This weight can be based on Gaussian distrubtion. 

# Thus ,sharp edges are preserved while discarding the weak ones. 


print("gaussian bluring:-->")


org_img=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\9.jpg")
res_size=cv2.resize(org_img,(300,400))

g=cv2.GaussianBlur(res_size,(7,7),0)
h=np.hstack((res_size,g))


cv2.imshow("Ishu",h)
cv2.waitKey(3000)
cv2.destroyAllWindows()

print()

print("Median bluring:-->")

org_img=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\9.jpg")
res_size=cv2.resize(org_img,(300,400))
m=cv2.medianBlur(res_size,5)
h=np.hstack((res_size,m,g))
cv2.imshow("ishu",h)
cv2.waitKey(10000)
cv2.destroyAllWindows()


print()
print("Bilateral bluring:-->")
org_img=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\New folder\9.jpg")
res_size=cv2.resize(org_img,(300,400))

b=cv2.bilateralFilter(res_size,9,75,75)
h=np.hstack((res_size,m,g,b))

cv2.imshow("ishu",h)
cv2.waitKey(10000)
cv2.destroyAllWindows()
