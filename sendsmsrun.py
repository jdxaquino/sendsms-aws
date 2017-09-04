#!/usr/bin/env python
import sys
import time
import serial

last_received = ''

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

argument = sys.argv

if len(argument) < 3:
    print 'Argumentos insuficientes: ./sendsms telefono mensaje'
    exit

phone_number= argument[1]+'\n'
text = argument[2:]


message=""
for word in text:
    message = message + word + " "

message = message + '\n'

# configure the serial connections (the parameters differs on the device you are connecting to)

print 'Connecting...'

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




print 'wake up'
ser.write('?\n')
receiving(ser)
if '@' in last_received:
    ser.write('\n')
    time.sleep(1)
    receiving(ser)
    #print 'enviando mensaje'
    ser.write(phone_number)
    print phone_number
    time.sleep(1)
    receiving(ser)
    ser.write(message)
    print message
    time.sleep(2)
    receiving(ser)
elif '#' in last_received:
    #print 'enviando mensaje'
    ser.write(phone_number)
    print phone_number
    time.sleep(1)
    receiving(ser)
    ser.write(message)
    print message
    time.sleep(2)
    receiving(ser)
print 'ok'



















