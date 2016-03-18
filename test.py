import RPi.GPIO as GPIO

import time,sys

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)

FREQ=100
MAX_DUTY=0.23*FREQ
MIN_DUTY=0.1*FREQ
MAX_ANGLE=90

print "Minimal Duty %s"%MIN_DUTY
print "Maximal Duty %s"%MAX_DUTY

pwm=GPIO.PWM(18,FREQ)
pwm.start(0)

def update(angle):
	new_angle = float(angle)
	duty=(MAX_DUTY-MIN_DUTY)*new_angle/float(MAX_ANGLE) + MIN_DUTY
	print "%s ==> %s"%(new_angle, duty)
	if duty > 100:
		print "Duty must be less than 100"
		duty = 100
	pwm.ChangeDutyCycle(duty)

DELAY=0.1
for j in range(0,100):
	try:
		for i in range(0,MAX_ANGLE):
			update(i)
			time.sleep(DELAY)
		for i in range(MAX_ANGLE,0,-1):
			update(i)
			time.sleep(DELAY)
	except:
		print "Exiting....!"
		GPIO.cleanup()
		sys.exit(1)

while True:
	try:
		angle = input("Angle?: ")
		#pwm.ChangeDutyCycle(float(angle))
		update(angle)
	except:
		print "Exiting....!"
		GPIO.cleanup()
		sys.exit(1)
	

