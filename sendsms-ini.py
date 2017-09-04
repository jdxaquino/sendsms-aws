#!/usr/bin/env python
import sys
import time
import serial
from datetime import datetime

last_received = ''

PATH='/home/jdxaquino/Documents/SWP/'

def log(text):
         now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
         with open(PATH+'serversms.log','a') as myfile:
                  myfile.write(now+' '+text+'\n')



def receiving(ser): 
    global last_received 
    buffer_string = '' 
    while True: 
        buffer_string = buffer_string + ser.read(ser.inWaiting()) 
        if '\n' in buffer_string: 
            lines = buffer_string.split('\n') #Guaranteed to have at least 2 entries 
            #print lines
            last_received = lines[-2] 
            #If the Arduino sends lots of empty lines, you'll lose the 
            #last filled line, so you could make the above statement conditional
            #like so: if lines[-2]: last_received = lines[-2] 
            buffer_string = lines[-1]
            break

    print last_received  

log('Running sendsms.py')

print 'Connecting...'
log('Connecting...') 
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)
#ser.open()
ser.isOpen()
time.sleep(1)
receiving(ser)
sys.exit()

















