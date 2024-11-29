import cv2
import numpy as np
from matplotlib import pyplot as plt

nrows = 2
ncols = 1

imgOrig = cv2.imread("ATU.jpg",)
imgGray = cv2.cvtColor(imgOrig, cv2.COLOR_BGR2GRAY)
imgHarris = cv2.imread("ATU.jpg",)

cv2.imshow('Atu Origional',imgOrig)
cv2.waitKey(0)
cv2.imshow('Grayscale',imgGray)
cv2.waitKey(0)

B = 10
G = 10
R = 10
blockSize = 2
aperture_size = 3
k = 0.03


dst = cv2.cornerHarris(imgHarris, blockSize, aperture_size, k)

threshold = 0.2; #number between 0 and 1
for i in range(len(dst)):
    for j in range(len(dst[i])):
        if dst[i][j] > (threshold*dst.max()):
            cv2.circle(imgHarris,(j,i),3,(B, G, R),-1)

