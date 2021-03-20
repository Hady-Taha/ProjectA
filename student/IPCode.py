import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt

class iris:

    def __init__(self,img):

        self.img = img

        

    def seg(self,img):

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Blur using 3 * 3 kernel.
        gray_blurred = cv2.blur(gray, (3, 3))

        # Apply Hough transform on the blurred image.
        detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 1, maxRadius = 40)

        # Draw circles that are detected.
        if detected_circles is not None:

            # Convert the circle parameters a, b and r to integers.
            detected_circles =  np.uint16(np.around(detected_circles))

            for pt in detected_circles[0, :]:
                a, b, r = pt[0], pt[1], pt[2]

                # Draw the circumference of the circle.
                cv2.circle(img, (a, b), r, (255, 255, 0), 2)

                # Draw a small circle (of radius 1) to show the center.
                cv2.circle(img, (a, b), 1, (255, 255, 0), 3)
                #cv2.imshow("Detected Circle", img)






    # Fun to find the keypoints to the new image from the register new student
    def toKP(self):
        sift = cv2.SIFT_create()
        kp1, des1 = sift.detectAndCompute(self.img,None)

        return des1

    # Fun to match between the object(the student iris from front end) and imgsKP (all Keypoints from database) and return the percentage of the matching
    def match(self,imgsKP):

        bf = cv2.BFMatcher()
        imgKP = self.toKP()



        matches = bf.knnMatch(imgKP,imgsKP,k=2)

        good = []
        for m,n in matches:
            if m.distance < 0.8*n.distance:
                good.append([m])

        x = len(imgKP)
        z = len(good)

        r = (z/x)*100
        #print("R = " + str(r) + " %")

        return r
            
