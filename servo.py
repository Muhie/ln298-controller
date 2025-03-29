# Raspberry Pi + MG90S Servo PWM Control Python Code
#
#
import RPi.GPIO as GPIO
import time

# setup the GPIO pin for the servo
servo_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)

# setup PWM process
pwm = GPIO.PWM(servo_pin,50) # 50 Hz (20 ms PWM period)

pwm.start(7) # start PWM by rotating to 90 degrees

for ii in range(0,3):
    pwm.ChangeDutyCycle(2.0) # rotate to 0 degrees
    time.sleep(0.5)
    pwm.ChangeDutyCycle(7.0) # rotate to 180 degrees
    time.sleep(0.5)
