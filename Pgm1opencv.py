import cv2

img = cv2.imread("img1.png")
cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()