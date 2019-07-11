# FaceID-Attendance-System
FaceMark is a Facial Recognition based Attendance system.

Problem Statement:  Time waste during Attendance in Classrooms 
Solution:  Facial Recognition based Attendance System (FaceMark)
Result: Reduce attendance taking time from 10 minutes to 10 seconds. (60X faster)


A normal university lecture is of 45 minutes, from which almost 10 minutes are taken by manual attendance. Now here, the goal is to minimize the time of attendance so that students can take maximum benefit from a teacher.

Now whats better solution than including cutting end technologies into it. So I did the same. I integrated Computer Vision, Neural Networks and Internet of Things and make a FaceID-based Attendance System which can mark the attendance of the whole class with just one click. It reduces attendance time from 10 minutes to 10 seconds(Including email sending to the Teachers).

This repository is consisting of several programs,lets discuss them on by one from where you are well known with haarcascade_classifier.

1. Dataset.ipynb: This program is responsible for collecting the dataset or facial images of students if you dont have the dataset. This will take a lot of pictures of their faces and save them in the specified folder which you need to specift in the Dataset.ipynb

2. CropFace.py: This program is responsible if you have the dataset and you only want to crop their faces from the dataset because we are only concern with the faces, This program will crop their faces and save them into a seperate folder.

3. Training.ipynb is the program which is responsible for training the whole dataset and daving their weights. You can manualy edit the classes from this file.

4. Student_log.txt is the master file from where the program is reading the roll numbers and names of the students.

5. weights.h5 is the saved weights of my dataset.

6. Marked.csv is the output file which is generated everytime attenance is taken.

7. Atte.py is the master file which mark the attendance of all the students, generate the attendance sheet, send it to the desired email address as written in the program. 

Signal.py is optional if you want to integrate it with IoT using blynk as i did or some device where teacher need to press the actual button of the device placed in the class and mark the attendance.

Thanks for Reading
Happy Learning
