from unittest import result
from cv2 import contourArea, detail_BundleAdjusterAffine
from matplotlib import image
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image,ImageOps
from os import listdir
from os.path import isfile, join
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import RandomizedSearchCV
import cv2
import predict as model
import math



source = 0
cap = cv2.VideoCapture(source)
"""
RGB -> Red Green Blue (normally)
BGR -> Blue Green Blue
HSV -> Hue saturation and Lightness/Brightness

"""
gsv = model.train()
result = 'null'
img_counter = 0
while(cap.isOpened()):


    ret,frame = cap.read()
    blurred_frame = cv2.GaussianBlur(frame,(5,5),0)
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(blurred_frame,cv2.COLOR_BGR2HSV) #change BGR to HSV
    lower_black = np.array([110,50,50])
    upper_black = np.array([130,255,255])
    res2 = cv2.inRange(hsv,lower_black,upper_black) #detect color blue

    contours, _ = cv2.findContours(res2,cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    sorted_contours = sorted(contours,key = cv2.contourArea,reverse=True)
    contours = (sorted_contours[:3])
    for contour in contours:
        area = cv2.contourArea(contour)
        if (area > 5000): #& (area == cv2.contourArea(biggest_contour))
            cv2.drawContours(res2,contour,-1,(0,255,0),3)
            cv2.drawContours(frame,contour,-1,(0,255,0),3)
            peri = cv2.arcLength(contour,True)
            approx = cv2.approxPolyDP(contour,0.01*peri,True)
            x,y,w,h = cv2.boundingRect(approx)
            cv2.rectangle(res2,(x-20,y-20),(x+w+20,y+h+20),(255,255,255),3)
            cv2.rectangle(frame,(x-20,y-20),(x+w+20,y+h+20),(0,255,0),5)
            imm = cv2.resize(res2,(640,480))
            roi = imm[y-20:y+h+20,x-20:x+w+20]
            try:
                crop_image = cv2.resize(roi,(8,8),interpolation = cv2.INTER_AREA)
                pixel = np.array(crop_image)/255*16
                pixel = pixel.astype('int')
                my_digit = pixel.reshape(1,-1)
                result = gsv.predict(my_digit)[0]

            except Exception as e:
                print(str(e))
            if cv2.waitKey(1)==ord('w'):
                img_name = "opencv_frame_{}.png".format(img_counter)
                try:
                    cv2.imwrite(img_name,roi)
                    img_counter+=1
                except Exception as e:
                    print(str(e))
            # plt.imshow(crop_image)


            cv2.putText(res2,"Points: "+str(len(approx)),(x+w+20,y+20),cv2.FONT_HERSHEY_COMPLEX,.7,(0,255,0),2)
            cv2.putText(frame,"Points: "+str(len(approx)),(x+w+20,y+20),cv2.FONT_HERSHEY_COMPLEX,.7,(0,255,0),2)
            cv2.putText(res2,"Predict: "+str(result),(x+w+20,y+45),cv2.FONT_HERSHEY_COMPLEX,.7,(0,255,0),2)
            cv2.putText(frame,"Predict: "+str(result),(x+w+20,y+45),cv2.FONT_HERSHEY_COMPLEX,.7,(0,255,0),2)
            
 
    cv2.imshow('res2',res2)
    cv2.imshow('frame',frame)
    # plt.show()

    if (cv2.waitKey(1)==ord('q') ):
        break
        
cap.release()
cv2.destroyAllWindows()