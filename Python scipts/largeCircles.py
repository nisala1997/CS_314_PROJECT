import numpy as np
import cv2
import matplotlib.pyplot as plt

try:
    # Read the image
    img = cv2.imread('B5.JPG', cv2.IMREAD_GRAYSCALE)

    # Apply median blurring
    img = cv2.medianBlur(img, 5)

    # Convert to color for visualization
    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    # Detect circles using Hough transform
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 120, param1=40, param2=50, minRadius=20, maxRadius=120)

    if circles is not None:
        # Convert the coordinates and radius to integers
        circles = np.uint16(np.around(circles))

        # Draw the detected circles
        for i in circles[0, :]:
            cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
            cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

        # Print the number of circles detected
        print(circles.shape[1])

        # Display the image
        cv2.namedWindow('fig', cv2.WINDOW_KEEPRATIO)
        cv2.imshow('fig', cimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:
        print("No circles detected in the image.")

except Exception as e:
    print("An error occurred:", str(e))


