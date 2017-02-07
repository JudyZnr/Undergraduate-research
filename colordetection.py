#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 21:01:47 2017

@author: administorzz
"""

import numpy as np
import cv2

img = cv2.imread("imgtest.png")

hsv = cv2.cvtColor(img.cv2.COLOR_BGR2HSV)

lower = np.array([])
upper = np.array([])

mask = cv2.inRange(hsv,lower,upper)

cv2.imshow('Image',img)
cv2.imshow('Result',mask)

cv2.waitKey(0)
cv2.destoryAllWindows()