import cv2
import numpy as np
from matplotlib import pyplot as plt

nrows = 2
ncols = 1

imgOrig = cv2.imread("ATU.jpg",)
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

maxCorners = 100
qualityLevel = 0.01
minDistance = 10

corners = cv2.goodFeaturesToTrack(imgGray,maxCorners,qualityLevel,minDistance)
corners = np.int0(corners) #convert corners values to integer

for i in corners:
    x,y = i.ravel()
    cv2.circle(imgShiTomasi,(x,y),3,(B, G, R),-1)
    
cv2.imshow('Shi Tomasi',imgShiTomasi)
cv2.waitKey(0)

imgOrb = imgGray.copy()
 
# Initiate ORB detector
orb = cv2.ORB_create()
 
# find the keypoints with ORB
kp = orb.detect(imgOrb,None)
 
# compute the descriptors with ORB
kp, des = orb.compute(imgOrb, kp)
 
# draw only keypoints location,not size and orientation
imgOrb2 = cv2.drawKeypoints(imgOrb, kp, None, color=(0,255,0), flags=0)
cv2.imshow('Orb Detection',imgOrb2)
cv2.waitKey(0)
