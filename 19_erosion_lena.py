import numpy as np
import cv2

img = cv2.imread('lena.bmp', cv2.IMREAD_GRAYSCALE)
height = img.shape[0]
width = img.shape[1]
print("erosion")
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel)
cv2.imwrite("erosion_lena.bmp", erosion )
cv2.imshow("original",img)
cv2.imshow("erosion",erosion)
cv2.waitKey()
cv2.destroyAllWindows()