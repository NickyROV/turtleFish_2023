from machine import Pin, UART, PWM
import time

uart=UART(1, baudrate=9600)
uart.init(bits=8, parity=None, stop=1)

fwd = 1700000		# in nanosecond
rev = 1300000
clawOpen = 1900000
clawClose = 1100000
halt = 1500000

thruster8=PWM(Pin(6), freq=100, duty_ns= halt)
thruster8=PWM(Pin(7), freq=100, duty_ns= halt)
thruster8=PWM(Pin(8), freq=100, duty_ns= halt)
thruster9=PWM(Pin(9), freq=100, duty_ns=halt)
thruster10=PWM(Pin(10), freq=100, duty_ns=halt)
thruster11=PWM(Pin(11), freq=100, duty_ns=halt)
claw12=PWM(Pin(12), freq=100, duty_ns=halt)
claw13=PWM(Pin(13), freq=100, duty_ns=halt)

def rise():
    thruster8.init(freq=100, duty_ns=fwd)
    thruster9.init(freq=100, duty_ns=fwd)
 
def sink():
    thruster8.init(freq=100, duty_ns=rev)
    thruster9.init(freq=100, duty_ns=rev)

def forward():
    thruster6.init(freq=100, duty_ns=fwd)
    thruster7.init(freq=100, duty_ns=fwd)
    thruster10.init(freq=100, duty_ns=fwd)
    thruster11.init(freq=100, duty_ns=fwd)

def reverse():
    thruster6.init(freq=100, duty_ns=rev)
    thruster7.init(freq=100, duty_ns=rev)
    thruster10.init(freq=100, duty_ns=rev)
    thruster11.init(freq=100, duty_ns=rev)

def goLeft():
    thruster6.init(freq=100, duty_ns=rev)
    thruster7.init(freq=100, duty_ns=fwd)
    thruster10.init(freq=100, duty_ns=rev)
    thruster11.init(freq=100, duty_ns=fwd)

def goRight():
    thruster6.init(freq=100, duty_ns=fwd)
    thruster7.init(freq=100, duty_ns=rev)
    thruster10.init(freq=100, duty_ns=fwd)
    thruster11.init(freq=100, duty_ns=rev)

def fwdLeft():
    thruster7.init(freq=100, duty_ns=fwd)
    thruster11.init(freq=100, duty_ns=fwd)

def fwdRight():
    thruster6.init(freq=100, duty_ns=fwd)
    thruster10.init(freq=100, duty_ns=fwd)

def revLeft():
    thruster6.init(freq=100, duty_ns=rev)
    thruster10.init(freq=100, duty_ns=rev)

def revRight():
    thruster7.init(freq=100, duty_ns=rev)
    thruster11.init(freq=100, duty_ns=rev)

def turnLeft():
    thruster6.init(freq=100, duty_ns=fwd)
    thruster7.init(freq=100, duty_ns=rev)
    thruster10.init(freq=100, duty_ns=rev)
    thruster11.init(freq=100, duty_ns=fwd)

def turnRight():
    thruster6.init(freq=100, duty_ns=rev)
    thruster7.init(freq=100, duty_ns=fwd)
    thruster10.init(freq=100, duty_ns=fwd)
    thruster11.init(freq=100, duty_ns=rev)

def stop():
    thruster6.init(freq=100, duty_ns=halt)
    thruster7.init(freq=100, duty_ns=halt)
    thruster8.init(freq=100, duty_ns=halt)
    thruster9.init(freq=100, duty_ns=halt)
    thruster10.init(freq=100, duty_ns=halt)
    thruster11.init(freq=100, duty_ns=halt)


while True:
    if uart.any():
        data=uart.read()
        print (data)
        if data==b'\xaa\xaa\xff' :
            rise()
        elif data==b'\xaa\xcc\xff':
            sink()        
        elif data==b'\xcc\xaa\xff':
            fwd()
        elif data==b'\xcc\xbb\xff':
            fwdLeft()
        elif data==b'\xcc\xcc\xff':
            fwdRight()            
        elif data==b'\xdd\xaa\xff':
            rev()
        elif data==b'\xdd\xcc\xff':
            revLeft()
        elif data==b'\xdd\xdd\xff':
            revRight()             
        elif data==b'\xcc\xdd\xff':
            goLeft()
        elif data==b'\xcc\xee\xff':
            goRight()             
        elif data==b'\xbb\xbb\xff':
            turnLeft()
        elif data==b'\xbb\xaa\xff':
            turnRight()            
        elif data==b'\xee\xaa\xff':
            claw12.init(freq=100, duty_ns=clawOpen)
        elif data==b'\xee\xbb\xff':
            claw12.init(freq=100, duty_ns=clawClose)
        elif data==b'\xee\xcc\xff':
            claw13.init(freq=100, duty_ns=clawOpen)
        elif data==b'\xee\xdd\xff':
            claw13.init(freq=100, duty_ns=clawClose)
        elif data==b'\xee\xee\xff':
            stop()
            
        time.sleep(0.01)
        
