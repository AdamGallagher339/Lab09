import cv2
import numpy as np
from matplotlib import pyplot as plt

nrows = 2
ncols = 1

imgOrig = cv2.imread("ATU1.jpg",)
imgGray = cv2.cvtColor(imgOrig, cv2.COLOR_BGR2GRAY)
imgHarris = imgOrig.copy()
imgShiTomasi = imgOrig.copy()

cv2.imshow('Atu Origional',imgOrig)
cv2.waitKey(0)
cv2.imshow('Grayscale',imgGray)
cv2.waitKey(0)

B = 0
G = 0
R = 255
blockSize = 2
aperture_size = 3
k = 0.03

dst = cv2.cornerHarris(imgGray, blockSize, aperture_size, k)

threshold = 0.2; #number between 0 and 1
for i in range(len(dst)):
    for j in range(len(dst[i])):
        if dst[i][j] > (threshold*dst.max()):
            cv2.circle(imgHarris,(j,i),3,(B, G, R),-1)

cv2.imshow('Image Harris',imgHarris)
cv2.waitKey(0)

maxCorners = 2
qualityLevel = 0.1
minDistance = 10

corners = cv2.goodFeaturesToTrack(imgGray,maxCorners,qualityLevel,minDistance)
corners = np.int0(corners) #convert corners values to integer

