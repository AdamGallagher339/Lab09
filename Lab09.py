import cv2
import numpy as np
from matplotlib import pyplot as plt

imgOrig = cv2.imread("ATU.jpg",)

imgGray = cv2.cvtColor(imgOrig, cv2.COLOR_BGR2GRAY)

