import RPi.GPIO as GPIO
import time
from distance import *
GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
sensor = Sensor()
# Pins used to configure the UltraSonic Sensor on the right side of the robot
TRIG_PIN_A = 16
ECHO_PIN_A = 18
IR_PIN = 11

# ================================================================ #
# =================== Ultrasonic Sensor PINS ===================== #
GPIO.setup(TRIG_PIN_A, GPIO.OUT)
GPIO.setup(ECHO_PIN_A, GPIO.IN)
GPIO.setup(IR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def get_data():
    right = sensor.ultrasonic(TRIG_PIN_A, ECHO_PIN_A)
    x = sensor.ir()
    return (right, x)


def main():
    try:
        while True:
            distance = get_data()
            GPIO.output(3, True)
            GPIO.output(5, True)
            GPIO.output(7, True)

            print(distance)

    except (KeyboardInterrupt, TypeError):
        GPIO.cleanup()
        print(" Cleanup successful")