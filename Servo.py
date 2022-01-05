#!/bin/Python3
import RPi.GPIO as GPIO
import time
import sys

Servo_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(Servo_pin, GPIO.OUT)

Servo = GPIO.PWM(Servo_pin, 50)

Servo.start(0)


def servo_angle(angle):
    duty = 2.5 + (12.0 - 2.5) * (angle + 90) / 180
    Servo.ChangeDutyCycle(duty)
    time.sleep(0.3)


while True:
    try:
        servo_angle(-90)
        servo_angle(-60)
        servo_angle(-30)
        servo_angle(0)
        servo_angle(30)
        servo_angle(60)
        servo_angle(90)

    except KeyboardInterrupt:
        Servo.stop()
        GPIO.cleanup()
        sys.exit()
