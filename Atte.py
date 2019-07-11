import smtplib
import os
import cv2 as cv
import numpy as np
import pandas as pd
from keras.models import load_model

faceCascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

font = cv.FONT_HERSHEY_SIMPLEX

model = load_model('weights.h5')

def clean_logs():
    
    prev_logs = os.listdir('Logs')

    for i in prev_logs:
        os.remove('Logs/'+ i)

def detect_faces(student_dict):
    
    cap = cv.VideoCapture(0)

    while True:

        ret, frame = cap.read()
        frame = cv.flip(frame, 1)
        
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale( gray , scaleFactor=1.2)


        for (x, y, w, h) in faces:
            
            cv.rectangle(frame, (x, y), (x+w, y+h), (122, 122, 122), 2)

#            img = frame[y : y + h, x : x + w]
#            img = img/255.0
#            img = cv.resize(img, (64,64))
#            img = np.reshape(img, (1,64,64,3))

#            pred = int(np.argmax(model.predict(img)))
#            present = pred + 1
#            present = str(student_dict[present])

#            cv.putText(frame, present, (x,y), font, 2, (0,0,255))

        cv.imshow('Video', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):

            i = 0
            for (x, y, w, h) in faces:
                i = i + 1
                cropped = frame[y : y + h, x : x + w]   
                name = 'Logs/' + str(i) + '.jpg'    
                cv.imwrite(name ,cropped)

            break

    cap.release()
    cv.destroyAllWindows()

def attendance():

    presents = []
    detected = os.listdir('Logs/')

    for img in detected:
        
        if img != '.DS_Store':
        
            img_name = 'Logs/'+ str(img)
            img = cv.imread(img_name).astype(float)
            img = img/255.0
            img = cv.resize(img, (64,64))
            img = np.reshape(img, (1,64,64,3))

            pred = np.argmax(model.predict(img))
            presents.append(pred + 1)    
        
    return sorted(presents)

def file_reader(presents):
#    student_dict = {}
    
    data = pd.read_csv('Student_log.txt').values
    data = data.tolist()
    
    for i in range(len(data)):

        if data[i][0] in presents:
            data[i][3] = 'Present'

        else:
            data[i][3] = 'Absent'
            
#        student_dict[data[i][0]] = data[i][2]
            
    return data


def student_key():
    student_dict = {}
    
    data = pd.read_csv('Student_log.txt').values
    data = data.tolist()
    
    for i in range(len(data)):
        student_dict[data[i][0]] = data[i][2]
            
    return student_dict


def file_generate(data):

    fd = open('Marked.csv','w')
    mail = ''
    print('--------------------------------------')
    for i in range(len(data)):
        
        mail = mail + str(data[i][0]) +'\t'+ str(data[i][1]) +'\t'+ str(data[i][2]) +'\t'+ str(data[i][3])
        mail = mail + '\n'
#        print(mail)
#        print(str(data[i][0]) +'\t'+ str(data[i][1]) +'\t'+ str(data[i][2]) +'\t'+ str(data[i][3]))
        fd.write(str(data[i][0]) +','+ str(data[i][1]) +','+ str(data[i][2]) +','+ str(data[i][3]))
        fd.write('\n')
    print(mail)
        
    print('--------------------------------------')
    fd.close()
    print('Marked.csv file sucessfully created!')
    print('--------------------------------------')
    
    return mail
    
    
def send_mail(mail):
    email = 'tst1234500@gmail.com'
    paswd = '123456789'

    try:
        server = smtplib.SMTP(host = 'smtp.gmail.com', port = 587)
        server.starttls()

        server.login(email,paswd)

        message = mail
#        server.sendmail(email,['mailtoinayath@gmail.com'],message)
	server.sendmail(email,['zangrajazz@gmail.com'],message)
        print('Mail send sucessfully')
        server.quit()

    except:
        print('Failed!')
    
    
clean_logs()

student_dict = student_key()
detect_faces(student_dict)  

presents = attendance()
data = file_reader(presents)
mail = file_generate(data)
send_mail(mail)
