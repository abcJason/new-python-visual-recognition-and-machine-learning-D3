import cv2

import cv2
o=cv2.imread("image\\lenaNoise.png")

r10=cv2.blur(o,(10,10))
cv2.imwrite("result10.jpg",r10)
img_blurred=cv2.imread("result10.jpg")
sharp_mask = cv2.GaussianBlur(r10,(0,0),100)
img_sharpened = cv2.addWeighted(img_blurred, 1.5,sharp_mask, -1.,0 )
cv2.imshow("blurred",img_blurred)
cv2.imshow("sharpening",img_sharpened)
cv2.waitKey()
cv2.destroyAllWindows()