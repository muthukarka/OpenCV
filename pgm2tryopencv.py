import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread("img1.png")

plt.imshow(img)

plt.waitforbuttonpress()
plt.close("all")
