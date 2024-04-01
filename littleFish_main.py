from machine import Pin, UART, PWM
import time

uart=UART(1, baudrate=9600)
uart.init(bits=8, parity=None, stop=1)

fwdFull = 1900000		# in nanosecond
fwdHalf = 1700000
revFull = 1100000
revHalf = 1300000
clawOpen = 1900000
clawClose = 1100000
halt = 1500000

thruster8=PWM(Pin(8), freq=100, duty_ns= halt)
thruster9=PWM(Pin(9), freq=100, duty_ns=halt)
thruster10=PWM(Pin(10), freq=100, duty_ns=halt)
thruster11=PWM(Pin(11), freq=100, duty_ns=halt)
claw12=PWM(Pin(12), freq=100, duty_ns=halt)

def riseFast():
    thruster8.init(freq=100, duty_ns=fwdFull)
    thruster9.init(freq=100, duty_ns=fwdFull)
 
def riseSlow():
    thruster8.init(freq=100, duty_ns=fwdHalf)
    thruster9.init(freq=100, duty_ns=fwdHalf)

def sinkFast():
    thruster8.init(freq=100, duty_ns=revFull)
    thruster9.init(freq=100, duty_ns=revFull)

def sinkSlow():
    thruster8.init(freq=100, duty_ns=revHalf)
    thruster9.init(freq=100, duty_ns=revHalf)
    
def fwdFast():
    thruster10.init(freq=100, duty_ns=fwdFull)
    thruster11.init(freq=100, duty_ns=fwdFull)
 
def fwdSlow():
    thruster10.init(freq=100, duty_ns=fwdHalf)
    thruster11.init(freq=100, duty_ns=fwdHalf)

def revFast():
    thruster10.init(freq=100, duty_ns=revFull)
    thruster11.init(freq=100, duty_ns=revFull)

def revSlow():
    thruster10.init(freq=100, duty_ns=revHalf)
    thruster11.init(freq=100, duty_ns=revHalf)
    
def turnLeft():
    thruster10.init(freq=100, duty_ns=fwdHalf)
    thruster11.init(freq=100, duty_ns=revHalf)

def turnRight():
    thruster10.init(freq=100, duty_ns=revHalf)
    thruster11.init(freq=100, duty_ns=fwdHalf)

def stop():
    thruster8.init(freq=100, duty_ns=halt)
    thruster9.init(freq=100, duty_ns=halt)
    thruster10.init(freq=100, duty_ns=halt)
    thruster11.init(freq=100, duty_ns=halt)
    claw12.init(freq=100, duty_ns=halt)
    claw13.init(freq=100, duty_ns=halt)

while True:
    if uart.any():
        data=uart.read()
        print (data)
        if data==b'\xaa\xaa\xff' :
            riseFast()
        elif data==b'\xaa\xbb\xff':
            riseSlow()
        elif data==b'\xaa\xcc\xff':
            sinkFast()
        elif data==b'\xaa\xdd\xff':
            sinkSlow()
        elif data==b'\xcc\xaa\xff':
            fwdFast()
        elif data==b'\xcc\xbb\xff':
            fwdSlow()
        elif data==b'\xdd\xaa\xff':
            revFast()
        elif data==b'\xdd\xbb\xff':
            revSlow()
        elif data==b'\xbb\xbb\xff':
            turnLeft()
        elif data==b'\xbb\xaa\xff':
            turnRight()
        elif data==b'\xee\xaa\xff':
            claw12.init(freq=100, duty_ns=clawOpen)
        elif data==b'\xee\xbb\xff':
            claw12.init(freq=100, duty_ns=clawClose)
        elif data==b'\xee\xee\xff':
            stop()
            
        time.sleep(0.01)
        
