import cv2


# 2. Reading an image

img1 = cv2.imread('./images/geisel.jpg') # Default condition or 1
print(img1.shape)  # (476, 640, 3)

img2 = cv2.imread('./images/geisel.jpg', 0) # Default condition
print(img2.shape)  # (476, 640)


# 3. Displaying an Image

# cv2.imshow("GrayGeisel", img2)
# cv2.waitKey(1000)
# cv2.destroyAllWindows()

# Since I cannot use cv2 to display an image on Windows, 
# I have displayed it on a jupyter notebook using the kernel Ipython interactive display
# numpy to convert datatypes to img uint8, and Image object

from PIL import Image
import numpy as np

cv2.imwrite('./images/img2_gray.png', img2)
# display(Image.fromarray(img2))


# 4. Edge Detection:

# (i) Sobel Filter

sobelx = cv2.Sobel(src=img1, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge
cv2.imwrite('./images/sobelx_img.png', sobelx)
# display(Image.open('./images/sobelx_img.png'))

# (ii) Sobel Filter

edge_canny = cv2.Canny(img1, 100, 200)
cv2.imwrite('./images/edge_canny_img.png', edge_canny)
# display(Image.open('./images/edge_canny_img.png'))

# Testing our knowledge 

# Question 1 : Reverting Blue color space

# openCV reads images as BGR (rather than standard RGB)
geisel = cv2.imread('./images/geisel.jpg')

inv_blue = np.array(geisel.copy())
inv_blue[:,:,0] = 255 - inv_blue[:,:,0]
cv2.imwrite('./images/inv_blue.png', inv_blue)
# display(Image.open('./images/inv_blue.png'))

# Question 2:

# The dimensions resized takes are (width, height)

geisel_resized = cv2.resize(geisel, (geisel.shape[0], int(geisel.shape[1]/2)), interpolation = cv2.INTER_AREA)

cv2.imwrite('./images/resized_geisel.png', geisel_resized)
# display(Image.open('./images/resized_geisel.png'))

