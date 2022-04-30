# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 11:57:06 2021

@author: SAIRAJ
"""
import os
import cv2
import numpy as np
from PIL import Image
from tkinter import *

face_cascade=cv2.CascadeClassifier('D:/instafilter/instafilter/haarcascade_frontalface_default.xml')
video=cv2.VideoCapture(0)
address = 'https://192.168.43.1:8080/video'
video.open(address)

while 1:
    ret,img=video.read()
   # print("pixel of rgb",img)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#To convert color to gray
  #  print("pixel of rgb",gray)
    faces=face_cascade.detectMultiScale(gray,
    scaleFactor = 1.1 ,
    minNeighbors = 5)
#    print("face angle",faces)
    for (x,y,w,h) in faces:
            #sampleN=sampleN+1
            img = cv2.ret(img,(x,y),(x+y,y+h),(0,255,0),3)
            cv2.imshow('img',img)
            cv2.waitKey(1)
            if key== ord('q'):
                break
            video.release()
            cv2.destroyAllWindows()
  
  