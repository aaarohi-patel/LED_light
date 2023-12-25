#Libraries
import RPi.GPIO as GPIO
from time import sleep

#disable the warnings
GPIO.setwarnings(False)

#select the GIO mode
GPIO.setmode(GPIO.BOARD)

#set to appropiate GPIO pin format
redPin=29
bluePin=31
greenPin=33
#connect the longest pin that is cathode to Ground pin 6

GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)

for i in range (1, 3):
    print("Red") 
    GPIO.output(redPin, GPIO.HIGH)
    sleep(0.5)  #delay in 5 sec
    GPIO.output(redPin, GPIO.LOW)
    sleep(0.5)  #delay in 5 sec
    
    print("Green")
    GPIO.output(greenPin, GPIO.HIGH)
    sleep(0.5)  #delay in 5 sec
    GPIO.output(greenPin, GPIO.LOW)
    sleep(0.5)  #delay in 5 sec
    
    print("Blue")
    GPIO.output(bluePin, GPIO.HIGH)
    sleep(0.5)  #delay in 5 sec
    GPIO.output(bluePin, GPIO.LOW)
    sleep(0.5)  #delay in 5 sec

GPIO.cleanup()
