from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import time
import atexit

pwm = PWM(0x60)
pwm.setPWMFreq(1000)

pwm.setPWM(2,0,1000)
