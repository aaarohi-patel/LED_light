import RPi.GPIO as GPIO 
from time import sleep


redLEDpin = 12 #long end pin connects to power
#connect shorter end to ground

def cleanBoard():
	print("Cleaning Board!")
	#clean the board; erase previous settings
	GPIO.cleanup()
  
  
def SetUp():
	GPIO.setwarnings(False)
	#setting all warnings to False
	#set GPIO to board mode
	GPIO.setmode(GPIO.BOARD)  #
	GPIO.setup(redLEDpin, GPIO.OUT)
	
def LEDon():
	GPIO.output(redLEDpin, GPIO.HIGH)
	#turning the light on


def LEDoff():
	GPIO.output(redLEDpin, GPIO.LOW)
	#turning the light off
	
def TestLED():
	for p in range(1,6):
		print("Red")
		LEDon()
		sleep(0.5) #delay by 5 seconds
		LEDoff()
		sleep(0.5) #delay by 5 seconds
		
		
		
if __name__ == "__main__":
	SetUp()
	TestLED()
	cleanBoard()
