import numpy as np
import cv2

img = cv2.imread('lena.bmp', cv2.IMREAD_GRAYSCALE)
height = img.shape[0]
width = img.shape[1]
print("closing")
kernel = np.ones((5,5),np.uint8)
close = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
cv2.imwrite("closing_lena.bmp", close )
cv2.imshow("original",img)
cv2.imshow("closing",close)
cv2.waitKey()
cv2.destroyAllWindows()