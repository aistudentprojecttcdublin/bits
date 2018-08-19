#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 18:31:35 2018

@author: CP
"""

# Begin by setting API Service Key
import os 
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/CP/Desktop/MachineLearning/Lazy/Google_Cloud_Access/MLproject1-696323ed5422.json"

# Body of code for video capture
import cv2
from google.cloud import vision
client = vision.ImageAnnotatorClient()

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()