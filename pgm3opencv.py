import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("img1.png")
RGB_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(RGB_img)

plt.waitforbuttonpress()
plt.close('all')