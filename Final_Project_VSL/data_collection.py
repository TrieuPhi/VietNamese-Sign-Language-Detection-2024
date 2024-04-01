import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

import os as oss
import traceback



capture = cv2.VideoCapture(0)
hd = HandDetector(maxHands=1)
hd2 = HandDetector(maxHands=1)

# count = len(oss.listdir("D:\\ASL\\Sign-Language-To-Text-and-Speech-Conversion\\AtoZ_3.1\\A\\"))
count = len(oss.listdir("Image_Alphabet/A"))


c_dir = 'A'

offset = 15
step = 1
flag=False
suv=0

white=np.ones((400,400),np.uint8)*255
cv2.imwrite("./white.jpg",white)

capture.release()
cv2.destroyAllWindows()