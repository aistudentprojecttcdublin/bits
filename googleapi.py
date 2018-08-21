#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 18:31:35 2018

@author: CP
"""

# ------------------------------------------
#           SECTION 1: DOES THIS
# ------------------------------------------

# Begin by importing Libraries
import os 
import string
import numpy as np
import cv2
import time

# Body of code for video capture
# Change to test git

# Allow time for camera turning on
cap = cv2.VideoCapture(0)
time.sleep(1)

photos_saved = 0
num_photos = 0
path = "/Users/CP/Desktop/MachineLearning/Lazy/ComputerVision Projects/Photos"

while(photos_saved == 0):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Save Frame into Directory
    cv2.imwrite(os.path.join(path , ("photo"+str(num_photos)+".jpg")), frame)
    
    # Increment Photo Counter
    num_photos = num_photos + 1
    
    # Repeat 20 times
    if num_photos >= 20:
        photos_saved = 1
    
    time.sleep(0.5)
    

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

