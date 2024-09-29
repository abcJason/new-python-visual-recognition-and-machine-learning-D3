import cv2
import numpy as np
lena=cv2.imread("lena.bmp",0)
r,c=lena.shape
key=np.random.randint(0,256,size=[r,c],dtype=np.uint8)
encryption=cv2.bitwise_xor(lena,key)
decryption=cv2.bitwise_xor(encryption,key)
cv2.imshow("lena",lena)
cv2.imshow("key",key)
cv2.imshow("encryption",encryption) # 加密
cv2.imshow("decryption",decryption) # 解密
cv2.waitKey()
cv2.destroyAllWindows()