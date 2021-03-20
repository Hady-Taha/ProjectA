import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt
from IPCode import iris  #call my class


#new image to save her KP in database
imgToDB = cv2.imread("001_1_1.jpg")
eyeToDB = iris(imgToDB)
kpToDB = eyeToDB.toKP()



# iris from front-end to test
imgNew = cv2.imread("001_1_1.jpg")
eyeNew = iris(imgNew)


print(eyeNew.match(kpToDB))



cv2.waitKey(0)
cv2.destroyAllWindows()