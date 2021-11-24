from time import sleep
import RPi.GPIO as GPIO

import sys

SNAPSHOT_NUMBER=sys.argv[0]
DELAY_SECONDS=sys.argv[1]
DATA_DIRECTORY=sys.argv[2]
SNAPSHOT_DIRECTORY=sys.argv[3]
SNAPSHOT_FILENAME=sys.argv[4]
SNAPSHOT_FULL_PATH=sys.argv[5]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Focus is 23, Trigger is 24. Focus must be connected to trigger the shutter.
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
print("Setting Pin 23 High, Focusing")
GPIO.output(23, GPIO.HIGH)
sleep(0.5)
print("Setting Pin 24 High, Triggering Shutter")
GPIO.output(24, GPIO.HIGH)
sleep(0.25)
print("Setting Pin 24 Low, Releasing Shutter")
GPIO.output(24, GPIO.LOW)
print("Setting Pin 23 Low, Releasing Focus")
GPIO.output(23, GPIO.LOW)

