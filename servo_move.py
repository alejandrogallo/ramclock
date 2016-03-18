#! /bin/env python

import RPi.GPIO as GPIO
import time,sys
import argparse


GPIOPIN=18
FREQ=100

MAX_PULSE_WIDTH=0.226
MIN_PULSE_WIDTH=0.042

MAX_ANGLE=180

parser = argparse.ArgumentParser(description="Move servo to some angle")
parser.add_argument("-v", "--verbose", help="Make the output verbose", action="store_true")
parser.add_argument("-a", help="Angle to move to (0 to ang_max (%s))"%MAX_ANGLE, action="store")
parser.add_argument("--ang-max", help="Maximal angle (default = %s)"%MAX_ANGLE, action="store", default=MAX_ANGLE)
parser.add_argument("--max-pulse-w", help="Maximal pulse width (default %s)"%MAX_PULSE_WIDTH, action="store", default=MAX_PULSE_WIDTH)
parser.add_argument("--min-pulse-w", help="Minimal pulse width (default %s)"%MIN_PULSE_WIDTH, action="store", default=MIN_PULSE_WIDTH)

def printv(arg1):
    """
    Verbose print
    """
    if VERBOSE:
        print(arg1)



if __name__=="__main__" :
    # Parse arguments
    args = parser.parse_args()

    MAX_ANGLE=float(args.ang_max)

    MAX_PULSE_WIDTH=float(args.max_pulse_w)
    MIN_PULSE_WIDTH=float(args.min_pulse_w)

    MAX_DUTY=MAX_PULSE_WIDTH*FREQ
    MIN_DUTY=MIN_PULSE_WIDTH*FREQ

    if args.verbose:
        print("Making the command verbose...")
        VERBOSE=True
    else:
        VERBOSE=False

    printv("Minimal pulse width %s"%MIN_PULSE_WIDTH)
    printv("Maximal pulse width %s"%MAX_PULSE_WIDTH)
    printv("Minimal Duty %s"%MIN_DUTY)
    printv("Maximal Duty %s"%MAX_DUTY)

    printv("Maximal angle %s"%MAX_ANGLE)

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(GPIOPIN, GPIO.OUT)
    pwm=GPIO.PWM(GPIOPIN,FREQ)
    pwm.start(0)

    def update(angle):
        new_angle = float(angle)
        duty=(MAX_DUTY-MIN_DUTY)*new_angle/float(MAX_ANGLE) + MIN_DUTY
        printv("%s ==> %s"%(new_angle, duty))
        if duty > 100:
                printv("Duty must be less than 100")
                duty = 100
        pwm.ChangeDutyCycle(duty)

    update(args.a)
    time.sleep(1)
    GPIO.cleanup()
    sys.exit(0)


