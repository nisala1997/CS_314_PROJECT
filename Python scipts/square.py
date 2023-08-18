# Imports the necessary libraries
import numpy as np
import cv2
import argparse

# Initializes variables
refPt = []   # An empty list to store the coordinates of the selected region of interest (ROI).
cropping = False   # A Boolean flag indicating whether the user is currently selecting the ROI.

# Defines the click_and_crop function.
# This function is the event handler for mouse events within the image window.
# Finally, it displays the updated image in the window.

def click_and_crop(event, x, y, flags, param):
        
	global refPt, cropping
	
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True

	elif event == cv2.EVENT_LBUTTONUP:
                
		refPt.append((x, y))
		cropping = False

		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		cv2.namedWindow("image",cv2.WINDOW_KEEPRATIO)
		cv2.imshow("image", image)

# Loads an image
image = cv2.imread('B12.jpg')
# Creates a copy of the original image
clone = image.copy()
cv2.namedWindow("image",cv2.WINDOW_KEEPRATIO)

# Sets up the mouse callback function
cv2.setMouseCallback("image", click_and_crop)


# Starts a loop to display the image and wait for user input
# If the 'r' key is pressed, the image is reset to the original by copying clone back to image.
# If the 'c' key is pressed, it breaks the loop and moves to the next section of the code.

while True:
	cv2.namedWindow('image',cv2.WINDOW_KEEPRATIO)
	cv2.imshow("image", image)
	key = cv2.waitKey(1) & 0xFF
	
	if key == ord("r"):
		image = clone.copy()
		
	elif key == ord("c"):
		break

#If the refPt list contains two points, it proceeds with the following steps.
if len(refPt) == 2:
	# It extracts the selected ROI from the clone image using array slicing based on the coordinates stored in refPt.
	roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
	# displays the extracted ROI 
	cv2.namedWindow('ROI',cv2.WINDOW_KEEPRATIO)
	cv2.imshow("ROI", roi)
	# converts the ROI to grayscale 
	roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
	#  creates a square-shaped kernel 
	kernel = np.ones((50,50),np.uint8)
	# applies median blurring to reduce noise 
	blur = cv2.medianBlur(roi,15)
	# applies thresholding to convert the image to binary
	ret,thresh=cv2.threshold(blur,127,255,cv2.THRESH_BINARY)
	# performs dilation on the binary image
	dilation = cv2.dilate(thresh,kernel,iterations = 1)
	# applies inverse binary thresholding to the dilated image
	ret,thresh1=cv2.threshold(dilation,127,255,cv2.THRESH_BINARY_INV)
	#creates a new window named "fig" and displays the final processed
	cv2.namedWindow('fig',cv2.WINDOW_KEEPRATIO)
	cv2.imshow("fig",thresh1)

	# finds contours in the image using findContours() function 
	contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	# Finally, it prints the number of contours detected (subtracting 3 to exclude the image border contours).
	print(len(contours))
	cv2.waitKey(0)

# any key press before closing the windows
cv2.destroyAllWindows()


