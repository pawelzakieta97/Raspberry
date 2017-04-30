#from Adafruit_MotorHAT
from Adafruit_MotorHAT.Adafruit_PWM_Servo_Driver import PWM

import atexit
import time

pow = 1000
iter = 20
dt=0.1

pwm = PWM(0x60)
pwm.setPWMFreq(1000)

def coil1(pow):
    pwm.setPWM(2, 0, pow)
    if (pow<0):
        pwm.setPWM(3,0,0)
        pwm.setPWM(4,4096,0)
        print ("cewka 1 -")
    else:
        pwm.setPWM(3, 4096, 0)
        pwm.setPWM(4, 0, 0)
        print ("cewka 1 +")
    if (pow==0):
        pwm.setPWM(3, 0, 0)
        pwm.setPWM(4, 0, 0)
        print ("cewka 1 null")
    
def coil2(pow): 
    pwm.setPWM(8, 0, pow)
    if (pow<0):
        pwm.setPWM(9,0,0)
        pwm.setPWM(10,4096,0)
        print ("cewka 2 -")
    else:
        pwm.setPWM(9, 4096, 0)
        pwm.setPWM(10, 0, 0)
        print ("cewka 2 +")
    if (pow==0):
        pwm.setPWM(3, 0, 0)
        pwm.setPWM(4, 0, 0)
        print ("cewka 2 null")

for i in range (1,iter):
    coil2(0)
    coil1(pow)
    time.sleep(dt)
    coil2(pow)
    coil1(pow)
    time.sleep(dt)
    coil2(pow)
    coil1(0)
    time.sleep(dt)
    coil2(pow)
    coil1(-pow)
    time.sleep(dt)
    coil2(0)
    coil1(-pow)
    time.sleep(dt)
    coil2(-pow)
    coil1(-pow)
    time.sleep(dt)
    coil2(-pow)
    coil1(0)
    time.sleep(dt)
    coil2(-pow)
    coil1(pow)
    time.sleep(dt)
    


def turnOffMotors():
    pwm.setPWM(3,0,0)
    pwm.setPWM(4,0,0)
    pwm.setPWM(9,0,0)
    pwm.setPWM(10,0,0)
    print ("kurwa koniec")

atexit.register(turnOffMotors)
