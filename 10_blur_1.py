import cv2
o=cv2.imread("image\\lenaNoise.png")
cv2.imshow("original",o)

# r3=cv2.blur(o,(3,3))
# cv2.imshow("result3",r3)

r5=cv2.blur(o,(5,5))
cv2.imshow("result5",r5)

# r9=cv2.blur(o,(9,9))
# cv2.imshow("result9",r9)

r=cv2.boxFilter(o,-1,(5,5)) 
cv2.imshow("result",r)

cv2.waitKey()
cv2.destroyAllWindows()

from django.utils.translation import pgettext_lazy