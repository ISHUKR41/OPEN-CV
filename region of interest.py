import cv2 
          

img=cv2.imread(r"C:\Users\ISHU\OneDrive\Desktop\OPEN CV\savejonny.jpg")
# because we save the image of the jonny sir by the name of savejonny thwn we mena path change kar diya hai and we don't nee dof imgresize so we can comment it 
#img=cv2.resize(img,(700,600))

# cv2.imwrite("savejonny.jpg",img)
# and we also donot need of imwrite function q ki uska kaam aab ho gya hai 


# AND AAB BARI HAI IMAGE KO CROP KARNA KI lets go

#img[y1:y2,x1:x2]
print(img.shape)

crop=img[10:250,295:415]


img[10:250,415:525]= crop

cv2.imshow("Img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()