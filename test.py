#from Adafruit_MotorHAT
from Adafruit_MotorHAT.Adafruit_PWM_Servo_Driver import PWM

import atexit
import time

PWMpin=2
in1=3
in2=4

pwm = PWM(0x60)
pwm.setPWMFreq(1000)
 
pwm.setPWM(2, 0, 1000)
pwm.setPWM(3, 4096, 0)
pwm.setPWM(4, 0, 0)

time.sleep(1)

def turnOffMotors():
    pwm.setPWM(in1,0,0)
    pwm.setPWM(in2,0,0)
    print ("kurwa koniec")

atexit.register(turnOffMotors)
