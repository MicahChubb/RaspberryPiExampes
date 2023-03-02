from PIL import Image
import pytesseract
import cv2
import os, sys, inspect #For dynamic filepaths
import numpy as np;

#Find the execution path and join it with the direct reference
def execution_path(filename):
  return os.path.join(os.path.dirname(inspect.getfile(sys._getframe(1))), filename)			

filename = execution_path("3_python-ocr.jpg")
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)

print(text)
