#!/usr/bin/python

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.8CV)

enable_pin = 18
coil_A_1_pin = 5
coil_A_2_pin = 6
coil_B_1_pin = 13
coil_B_2_pin = 19

GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(enable_pin = 18)
GPIO.setup(coil_A_1_pin = 5)
GPIO.setup(coil_A_2_pin = 6)
GPIO.setup(coil_B_1_pin = 13)
GPIO.setup(coil_B_2_pin = 19)
GPIO.output(enable_pin, 1)

def forward (delay, steps ):
    for i in range (0, steps) :
    setStep(1,0,1,0)
    time.sleep(delay)
    setStep(0,1,1,0)
    time.sleep(delay)
    setStep(0,1,0,1)
    time.sleep(delay)
    setStep(1,0,0,1)
    time.sleep(delay)
def backwards (delay, steps ):
    for i in range (0, steps) :
    setStep(1,0,0,1)
    time.sleep(delay)
    setStep(0,1,0,1)
    time.sleep(delay)
    setStep(0,1,1,0)
    time.sleep(delay)
    setStep(1,0,1,0)
    time.sleep(delay)

def setStep(w1, w2,w3,w4)
GPIO.output(coil_A_1_pin, w1)
GPIO.output(coil_A_2_pin, w2)
GPIO.output(coil_B_1_pin, w3)
GPIO.output(coil_B_2_pin, w4)

while True :
    delay = 2.2
    #test input ("Delay between steps (milliseconds)?")
    steps = 512
    #test input ("Combien de pas avant")
    forward(int(delay) / 1000.0, int(steps))

GPIO.cleanup()
