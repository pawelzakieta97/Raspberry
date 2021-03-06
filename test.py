#from Adafruit_MotorHAT
from Adafruit_MotorHAT.Adafruit_PWM_Servo_Driver import PWM

import atexit
import time

pow = 4000
iter = 20000
dt=0.1

pwm = PWM(0x60)
pwm.setPWMFreq(1000)

def coil1(pow):
    
    if (pow<0):
        pwm.setPWM(3,0,4096)
        pwm.setPWM(4,4096,0)
        pwm.setPWM(2, 0, -pow)
        print ("cewka 1 -")
    if (pow>0):
        pwm.setPWM(3, 4096, 0)
        pwm.setPWM(4, 0, 4096)
        pwm.setPWM(2, 0, pow)
        print ("cewka 1 +")
    if (pow==0):
        pwm.setPWM(3, 0, 0)
        pwm.setPWM(4, 0, 0)
        pwm.setPWM(2, 0, pow)
        print ("cewka 1 null")
    
def coil2(pow): 
    pwm.setPWM(8, 0, pow)
    if (pow<0):
        pwm.setPWM(9,0,4096)
        pwm.setPWM(10,4096,0)
        pwm.setPWM(8, 0, -pow)
        print ("cewka 2 -")
    if (pow>0):
        pwm.setPWM(9, 4096, 0)
        pwm.setPWM(10, 0, 4096)
        pwm.setPWM(8, 0, pow)
        print ("cewka 2 +")
    if (pow==0):
        pwm.setPWM(3, 0, 0)
        pwm.setPWM(4, 0, 0)
        pwm.setPWM(8, 0, pow)
        print ("cewka 2 null")

def halfStep():
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
def fullStep():
    for i in range (1,iter):
        coil2(pow)
        coil1(0)
        time.sleep(dt)
        coil2(0)
        coil1(pow)
        time.sleep(dt)
        coil2(-pow)
        coil1(0)
        time.sleep(dt)
        coil2(0)
        coil1(-pow)
        time.sleep(dt)
        
def test():
    for i in range (1,iter):
        coil2(0)
        coil1(pow)
        time.sleep(2)
        coil2(0)
        coil1(-pow)
        time.sleep(2)
        coil1(0)
        coil2(pow)
        time.sleep(2)
        coil1(0)
        coil2(-pow)
        time.sleep(2)
    

def turnOffMotors():
    pwm.setPWM(3,0,0)
    pwm.setPWM(4,0,0)
    pwm.setPWM(9,0,0)
    pwm.setPWM(10,0,0)
    print ("koniec")
    
halfStep()
atexit.register(turnOffMotors)
