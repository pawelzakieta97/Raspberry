#from Adafruit_MotorHAT
from Adafruit_MotorHAT.Adafruit_PWM_Servo_Driver import PWM

import atexit
import time

pow = 1000
iter = 1000


pwm = PWM(0x60)
pwm.setPWMFreq(1000)

def coil1(pow): 
    pwm.setPWM(2, 0, pow)
    pwm.setPWM(3, 4096, 0)
    pwm.setPWM(4, 0, 0)
    
def coil2(pow): 
    pwm.setPWM(8, 0, pow)
    pwm.setPWM(9, 4096, 0)
    pwm.setPWM(10, 0, 0)

for i in range (1,iter):
    coil2(0)
    coil1(pow)
    time.sleep(0.01)
    coil1(0)
    coil2(pow)
    time.sleep(0.01)

time.sleep(10)

def turnOffMotors():
    pwm.setPWM(3,0,0)
    pwm.setPWM(4,0,0)
    pwm.setPWM(9,0,0)
    pwm.setPWM(10,0,0)
    print ("kurwa koniec")

atexit.register(turnOffMotors)
