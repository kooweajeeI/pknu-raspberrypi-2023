# LED 깜빡이기
import RPi.GPIO as GPIO
import time

signal_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(signal_pin, GPIO.OUT)

while(True):
    GPIO.output(signal_pin, True)
    time.sleep(2)
    GPIO.output(signal_pin, False)
    time.sleep(1)