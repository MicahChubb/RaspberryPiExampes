import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

# We need 3 pins per motor just like in Arduino, In pins control direction, En pins control speed
in1 = 22
in2 = 23
in3 = 20
in4 = 21
ena = 24 #PWM
enb = 26 #PWM

# Motor 1
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(ena, GPIO.OUT)

# Motor 2
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(enb, GPIO.OUT)

#Set in pins initially to low
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)

# Set up PWM on these pins
p1 = GPIO.PWM(ena,1000)
p2 = GPIO.PWM(enb,1000)

# Speed variable
speed = 100

# Starts the PWM at selected duty cycle
p1.start(speed)
p2.start(speed)

while(True):
    print(speed)
    
    # Change duty cycle to the new speed
    p1.ChangeDutyCycle(speed)
    p2.ChangeDutyCycle(speed)
    
    # Choose direction of motor
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)

    time.sleep(1)

    #Turn motors off
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    
    time.sleep(1)

    # Edit speed
    if(speed <= 0):
        speed = 100
    else:
        speed -= 5
