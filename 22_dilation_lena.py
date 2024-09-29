import numpy as np
import cv2

img = cv2.imread('lena.bmp', cv2.IMREAD_GRAYSCALE)
height = img.shape[0]
width = img.shape[1]
print("dilation")
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(img,kernel)
cv2.imwrite("dilation_lena.bmp", dilation )
cv2.imshow("original",img)
cv2.imshow("dilation",dilation)
cv2.waitKey()
cv2.destroyAllWindows()