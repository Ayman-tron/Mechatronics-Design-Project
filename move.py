import time
import RPi.GPIO as GPIO
from definitions import *
GPIO.setmode(GPIO.BOARD)

# Robot class with functions that allow Robot to move forward, backward, left and right


class Robot:

    # Both motors are rotating forward

    def forward(self, distance):
        # Motor # 1
        # Creating a PWM object
        myPWM = GPIO.PWM(ENA_PIN, 100)
        myPWM.start(99)

        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)

        # Motor # 2
        myPWM2 = GPIO.PWM(ENB_PIN, 100)
        myPWM2.start(99)
    #    myPWM.ChangeFrequency(1000)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH)

        # Time measurement is in seconds
        time.sleep(distance*1)
        self.stop()

    # Both motors are rotating backward

    def backward(self, distance):
        myPWM = GPIO.PWM(ENA_PIN, 100)
        myPWM.start(60)
        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN1, GPIO.LOW)
    #  myPWM.ChangeDutyCycle(99)
        myPWM2 = GPIO.PWM(ENB_PIN, 100)
        myPWM2.start(60)

        GPIO.output(IN4, GPIO.LOW)
        GPIO.output(IN3, GPIO.HIGH)

        time.sleep(distance*1)
        self.stop()

    # Right motor runs backward while left motor runs forward

    def right(self, distance):
        myPWM = GPIO.PWM(ENA_PIN, 100)
        myPWM.start(20)

        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN1, GPIO.LOW)

        myPWM2 = GPIO.PWM(ENB_PIN, 100)
        myPWM2.start(20)

        GPIO.output(IN4, GPIO.HIGH)
        GPIO.output(IN3, GPIO.LOW)

        time.sleep(distance*1)
        self.stop()

    # Right motor runs forward while left motor runs backward

    def left(self, distance):
        myPWM = GPIO.PWM(ENA_PIN, 100)
        myPWM.start(10)

        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN1, GPIO.HIGH)

        myPWM2 = GPIO.PWM(ENB_PIN, 100)
        myPWM2.start(10)

        GPIO.output(IN4, GPIO.LOW)
        GPIO.output(IN3, GPIO.HIGH)

        time.sleep(distance*1)
        self.stop()

    def stop(self):
        myPWM = GPIO.PWM(3, 100)
        myPWM.start(10)

        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN1, GPIO.LOW)

        myPWM2 = GPIO.PWM(5, 100)
        myPWM2.start(10)

        GPIO.output(IN4, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)

        time.sleep(5)

    def reset(self):
        # Cleaning up the GPIO pin for next user
        GPIO.cleanup()
