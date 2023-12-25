#imported libraries
import RPi.GPIO as GPIO
import time



#PIN SETUP
# ===== Accel & Gyro sensor pin setting ==================
# Import the MPU6050 class from the MPU6050.py file
from mpu6050 import mpu6050
#from machine import Pin, I2C

# AccelGyro pin connection information
# AccelGyro SCL connect to the pin# 5
# AccelGyro SDA connect to the pin# 3
# AccelGyro connet pin 1 to VCC
# AccelGyro connet pin 6 to ground

# ===== LED sensor pin setting ==================
redLedPin=12  #long leg of the LED
#connect the smaller leg to Ground pin 6

# ===== distance sensor pin setting ==================
distSensorTrigPin = 16
distSensorEchoPin = 18
# distance sensor connect the grn pin to GROUND (for example: pin 6)
# distance sensor connect the VCC pin to 5v pin#2

# ===== Buzzer Pin sensor pin setting ==================
#set buzzer - pin 22
buzzerPin = 22
#set ground to pin 6

# ===== tilt sensor pin setting ==================
leftTiltPin = 29
rightTiltPin = 31
# tilt sensor connect the grn pin to GROUND (for example: pin 6)
# tilt sensor connect the VCC pin to 5v pin#2

#variables
sensor = mpu6050(0x68)


def setup():
    # Disable warnings (optional)
    GPIO.setwarnings(False)
    # set the GPIO to the BOARD mode
    GPIO.setmode(GPIO.BOARD)
    # ===== LED sensor pin setting ==================
    GPIO.setup(redLedPin, GPIO.OUT)
    # ===== buzzer pin setting ==================
    GPIO.setup(buzzerPin, GPIO.OUT)
    # ===== distance sensor pin setting ==================
    GPIO.setup(distSensorTrigPin, GPIO.OUT)
    GPIO.setup(distSensorEchoPin, GPIO.IN)
    # ====== tilt sensor ==================
    GPIO.setup(leftTiltPin, GPIO.IN)
    GPIO.setup(rightTiltPin, GPIO.IN)

def cleanBoard():
    print("Cleaning up!")
    # Release resources - clean up the board setting
    GPIO.cleanup()

def checkLeftTilt():
    isTilted = False
    if (GPIO.input(leftTiltPin)):
        return True
    else:
        return False

def checkRightTilt():
    isTilted = False
    if (GPIO.input(rightTiltPin)):
        return True
    else:
        return False

def LEDOn():
    value = None
    GPIO.output(redLedPin, GPIO.HIGH)

    
def LEDOff():
    GPIO.output(redLedPin, GPIO.LOW)
    
def BeepOn():
    GPIO.output(buzzerPin, GPIO.HIGH)
    
def BeepOff():
    GPIO.output(buzzerPin, GPIO.LOW)


def distance(measure='cm'):
    try:
        GPIO.output(distSensorTrigPin, False)
        print("please wait a few seconds for the distance sensor to settle.")
        time.sleep(1)
        GPIO.output(distSensorTrigPin, True)
        time.sleep(0.00001)
 
        GPIO.output(distSensorTrigPin, False)
        #this is a loop that allows us to record the last timestamp before the signal reaches the receiver.
        while GPIO.input(distSensorEchoPin) == 0:
            noSignal = time.time()
 
        #here we register the last timestamp at which the receiver detects the signal. Namely,
        # the receiver will start receiving a direct signal until the reflected signal is finally received.
        while GPIO.input(distSensorEchoPin) == 1:
            signal = time.time()
 
        #we calculate the time difference between both timestamps
        timeLapse = signal - noSignal
 
        if measure == 'cm':
            distance = timeLapse / 0.000058
        elif measure == 'in':
            distance = timeLapse / 0.000148
        else:
            print('improper choice of measurement: in or cm')
            distance = None
        return round(distance)
    except:
        distance = -1
        return distance
    
    
def getUserArmLength():
    userArmLength = 0
    
    while True:
        try:
            userArmLength = int(input("Input the user's arm distance in cm: "))
        except ValueError:
            print("\nYou're inputted value is not an integer. Please try again")
            continue
        if userArmLength in range(50,120):
            return userArmLength
            break
        else:
            print("\nYour inputted value is not in the correct range. Please try again.")

def AlertOn():
    BeepOn()
    LEDOn()
    time.sleep(0.5)


def clearAlert():
    BeepOff()
    LEDOff()


def SitStraight():
    ArmLength = getUserArmLength()
    print("\nThe user should approximateley " + str(ArmLength) + " cm away from the monitor.")
    
    try:
        while True:
            '''
            if checkLeftTilt() or checkRightTilt() or (RealDistance not in range((ArmLength - 5),(ArmLength + 5))):
                AlertOn()
                continue
            else:
                AlertClear()
                continue
          
            if checkLeftTilt():
                print("Left tilted\n")
                AlertOn()
            else:
                print("Horizontal\n")
                clearAlert() 
            if checkRightTilt():    
                print("Right tilted\n")
                AlertOn()
            else:
                print("Horizontal\n")
                clearAlert()
            time.sleep(1)
        '''    
            
            RealDistance = distance('cm')
            print(str(RealDistance) + ' cm')
            if RealDistance not in range((ArmLength - 10),(ArmLength + 10)):
                AlertOn()
                continue
            else:
                clearAlert()
            time.sleep(0.5)
             
    except KeyboardInterrupt:  # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program
        clearAlert()
    
# main part
if __name__ == "__main__":
    setup()
    SitStraight()
    cleanBoard()  
