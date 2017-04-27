#from Adafruit_MotorHAT
from Adafruit_MotorHAT import Adafruit_MotorHAT
 
pwm = PWM(0x60)
pwm.setPWMFreq(1000)
 
pwm.setPWM(2, 0, 1000)
pwm.setPWM(3, 4096, 0)
pwm.setPWM(4, 0, 0)
