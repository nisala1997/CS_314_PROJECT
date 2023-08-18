import numpy as np
import cv2

img = cv2.imread('B12.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.medianBlur(img, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(
    img,
    cv2.HOUGH_GRADIENT,
    1,
    50,
    param1=30,
    param2=30,
    minRadius=1,  # Adjust the minimum radius as per your requirement
    maxRadius=15  # Adjust the maximum radius as per your requirement
)

if circles is not None:
    circles = np.uint16(np.around(circles))
    
    for i in circles[0, :]:
        cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
    
    print(circles.shape[1])

cv2.namedWindow('detected circles', cv2.WINDOW_KEEPRATIO)
cv2.imshow('detected circles', cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
