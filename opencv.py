import cv2
img=cv2.imread('ui.png')

ret,bw=cv2.threshold(img,127,255,cv2.COLOR_RGB2LUV)
cv2.imshow("Binary Image",bw)
cv2.waitKey(0)
cv2.destroyAllWindows()