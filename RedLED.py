#Libraries
import RPi.GPIO as GPIO
from time import sleep


# Sensors pins setting
# ===== LED sensor pin setting ==================
redLedPin=12  #long leg of the LED
#connect the smaller leg to Ground pin 6

def cleanBoard():
    print("Cleaning up!")
    # Release resources - clean up the board setting
    GPIO.cleanup()


def setup():
    # Disable warnings (optional)
    GPIO.setwarnings(False)
    # set the GPIO to the BOARD mode
    GPIO.setmode(GPIO.BOARD)
    # ===== LED sensor pin setting ==================
    GPIO.setup(redLedPin, GPIO.OUT)
   

def LEDOn():
    GPIO.output(redLedPin, GPIO.HIGH)
    
def LEDOff():
    GPIO.output(redLedPin, GPIO.LOW)

def TestLED():
    for i in range (1, 6):
        print("Red")
        LEDOn()
        sleep(0.5)  #delay in 5 sec
        LEDOff()
        sleep(0.5)  #delay in 5 sec
    
# main part
if __name__ == "__main__":
    setup()
    TestLED()
    cleanBoard()
    
