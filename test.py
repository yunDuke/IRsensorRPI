import RPi.GPIO as GPIO
import time
sensor = 7
#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.setup(18, GPIO.OUT)         
         #LED output pin
while True:
       i=GPIO.input(7)
       if i==0:                 #When output from motion sensor is LOW
             print "DETECTED"
             GPIO.output(18, 1)  #Turn OFF LED
             time.sleep(0.1)
       elif i==1:               #When output from motion sensor is HIGH
             print "NOTHING"
             GPIO.output(18, 0)  #Turn ON LED
             time.sleep(0.1)
