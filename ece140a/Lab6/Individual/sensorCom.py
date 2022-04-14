#!/usr/bin/python3
from signal import signal, SIGTERM, SIGHUP
from smbus import SMBus
import RPi.GPIO as GPIO
import time

bus = SMBus(1)
commands = (0x84, 0xc4, 0x94, 0xd4, 0xa4, 0xe4, 0xb4, 0xf4)

ledPin = 40 
trigPin = 23
echoPin = 24
MAX_DISTANCE = 220
timeOut = MAX_DISTANCE*60
buzzerPin = 6

def pulseIn(pin, level, timeOut):
    t0 = time.time()
    while(GPIO.input(pin) != level):
        if((time.time() - t0) > timeOut*0.000001):
            return 0
    t0 = time.time()
    while(GPIO.input(pin) == level):
        if((time.time() - t0) > timeOut*0.000001):
            return 0

    pulseTime = (time.time()-t0)*1000000
    return pulseTime


def getSonar():
    GPIO.output(trigPin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigPin, GPIO.LOW)
    pingTime = pulseIn(echoPin, GPIO.HIGH, timeOut)
    distance = pingTime*340.0/2.0/10000.0
    return round(distance,2)

def safe_exit(signum, frame):
    exit(1)


def joystick(input):
    bus.write_byte(0x4b, commands[input])
    return bus.read_byte(0x4b)

def ledOn():
    GPIO.output(ledPin, GPIO.HIGH) 

def ledOff():
    GPIO.output(ledPin, GPIO.LOW) 

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(trigPin, GPIO.OUT)
    GPIO.setup(echoPin, GPIO.IN)
    GPIO.setup(buzzerPin, GPIO.OUT)
    GPIO.setup(ledPin, GPIO.OUT) 
    GPIO.output(ledPin, GPIO.LOW) 
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)
