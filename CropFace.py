import os
import cv2 as  cv
import numpy as np

dir_name = 'Ashish/'
face_cascade = cv.CascadeClassifier('helper/haarcascade_frontalface_default.xml')
i = 0;

images = os.listdir(dir_name)

for image in images:
    try:
        img_path = dir_name + str(image)

        img = cv.imread(img_path)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        for (x,y,w,h) in faces:
            cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w - 4]
            roi_color = img[y:y+h, x:x+w - 4]

	    i = i + 1
	    cropped_img_path = 'Cropped/'+str(i)+str('.jpg') 

	    cv.imwrite(cropped_img_path,roi_color)

            print(i)

    except:
        pass