#!/usr/bin/env python

import os
import sys
import subprocess
from datetime 
import datetime

PATH='/home/jdxaquino/Documents/SWP/'

def log(text):
         now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
         with open(PATH+'serversms.log','a') as myfile:
                  myfile.write(now+' '+text+'\n')

log('Running Serversms...')
s1 = os.path.getsize(PATH+'message.txt')
s2 = os.path.getsize(PATH+'last-message.txt')
m1 = open(PATH+'message.txt', 'r+')
mc1 = m1.read()

if (s1 != s2):
         log('Message Change!')
         m2 = open(PATH+'last-message.txt', 'w+')
         m2.write(str(mc1))
         log('Sending SMS...')
         pid = subprocess.Popen([sys.executable, PATH+'/sendsms.py', '9626210908', str(mc1)])
         pid.wait()
         log('Ok')
         m2.close()
         m1.close()
else:
         m2 = open(PATH+'/last-message.txt', 'w+')
         m2.write(str(mc1))
         m2.close()
         m1.close()
