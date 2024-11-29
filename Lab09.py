import cv2
import numpy as np
from matplotlib import pyplot as plt

nrows = 2
ncols = 1

imgOrig = cv2.imread("ATU.jpg",)
imgGray = cv2.cvtColor(imgOrig, cv2.COLOR_BGR2GRAY)

cv2.imshow('Atu Origional',imgOrig)
cv2.waitKey(0)
cv2.imshow('Grayscale',imgGray)
cv2.waitKey(0)

