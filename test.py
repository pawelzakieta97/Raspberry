#from Adafruit_MotorHAT
from Adafruit_MotorHAT.Adafruit_PWM_Servo_Driver import PWM

import atexit

pwm = PWM(0x60)
pwm.setPWMFreq(1000)
 
pwm.setPWM(2, 0, 1000)
#pwm.setPWM(3, 4096, 0)
#pwm.setPWM(4, 0, 0)

def turnOffMotors():
    pwm.setPWM(2,0,4096)

atexit.register(turnOffMotors)
