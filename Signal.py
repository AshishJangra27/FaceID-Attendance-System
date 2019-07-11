from serial import Serial
import time
import os

ser = Serial('/dev/cu.SLAB_USBtoUART' , baudrate = 9600)

number = ser.read()
os.system('say Starting Program')
os.system('say Please Wait')

print('Initializing Program...')
os.system('say Openning Camera')
os.system('python atte.py')
print('Attendance Marked Successfully!')

os.system('say Attendance Marked Successfully')
os.system('say Email Sent Successfully')


