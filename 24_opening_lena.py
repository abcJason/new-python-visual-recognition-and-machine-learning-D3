import numpy as np
import cv2

img = cv2.imread('lena.bmp', cv2.IMREAD_GRAYSCALE)
height = img.shape[0]
width = img.shape[1]
print("opening")
kernel = np.ones((5,5),np.uint8)
open = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
cv2.imwrite("opening_lena.bmp", open )
cv2.imshow("original",img)
cv2.imshow("opening",open)
cv2.waitKey()
cv2.destroyAllWindows()