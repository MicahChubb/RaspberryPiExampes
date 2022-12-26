import cv2
import os, sys, inspect #For dynamic filepaths
import numpy as np;

#Find the execution path and join it with the direct reference
def execution_path(filename):
  return os.path.join(os.path.dirname(inspect.getfile(sys._getframe(1))), filename)			

img = cv2.imread(execution_path("animals.jpg"), cv2.IMREAD_GRAYSCALE)

# You can use this code to scale your image, my image was huge!
scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# I have commented out all but threshold parameters
# Uncomment each to have a look at how each parameter influences detection
# Definitions of parameters:
# https://learnopencv.com/blob-detection-using-opencv-python-c/

# Change thresholds
params.minThreshold = 10
params.maxThreshold = 200

# Filter by Area.
#params.filterByArea = True
#params.minArea = 10

# Filter by Circularity
#params.filterByCircularity = True
#params.minCircularity = 0.01
#params.maxCircularity = 0.7

# Filter by Convexity
#params.filterByConvexity = True
#params.minConvexity = 0.87

# Filter by Inertia
#params.filterByInertia = True
#params.minInertiaRatio = 0.01

# Filter by Colour
#params.filterByColor = 1
#params.blobColor = 255 

# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)


# Detect blobs.
keypoints = detector.detect(resized)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

im_with_keypoints = cv2.drawKeypoints(resized, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show blobs
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
