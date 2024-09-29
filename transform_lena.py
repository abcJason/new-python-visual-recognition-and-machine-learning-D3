import cv2
import numpy as np
img=cv2.imread("lena.bmp")
height,width=img.shape[:2]
print(height,width)

pts1 = np.float32([[0,0],[height,0],[0,width],[height,width]])
pts2 = np.float32([[0,0],[height,100],[0,511],[height,width+50]])

M=cv2.getPerspectiveTransform(pts1,pts2)
dst=cv2.warpPerspective(img,M,(width,height))
cv2.imshow("img",img)
cv2.imshow("dst",dst)
cv2.waitKey()
cv2.destroyAllWindows()
