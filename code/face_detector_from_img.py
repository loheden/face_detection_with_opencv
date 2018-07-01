#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 22:03:18 2018

@author: cesncn
"""

'''
The following code reads images from the given input directory, detects faces
in each given image, and saves just the face piece of the image in a new image
file in the output directory
'''

import cv2


input_dir = '../images/input_imgs/Z/'
output_dir = '../images/output_imgs/Z/'
faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

num_input_images = 1
counter = 1

for i in range(1, num_input_images):
    img_path = input_dir + 'z' + str(i) + '.jpg'
    img = cv2.imread(img_path)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print('gray.shape: ', gray.shape)
    faces = faceDetector.detectMultiScale(gray, 1.1, 5)
    for (x,y,w,h) in faces:
        #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        sub_face = img[y:y+h, x:x+w]
        face_file_name = output_dir + "z" + str(counter) + ".JPG"
        counter += 1
        cv2.imwrite(face_file_name, sub_face)
