# turtleFish
This project intended to build a simple 3 phase thruster driven ROV with Touch Screen as interface.

Top side Hardware :

Touch screen Human Machine Interface (HMI)

RS485 module (Modulation)

Tether : 15m

Underwater Hardware :

RS485 module (Demodulation)

RP2040 ARM Cortex M0 MCU (Raspberry Pi Pico)

Servo Driver Break out board (https://www.waveshare.com/wiki/Pico-Servo-Driver)

4x(ESC + T200 Bluerobotic Thruster)

Thruster 1 Upward Left (GPIO8) / Thruster 1 & 2 are in-phase

Thruster 2 Upward Right (GPIO9) / Thruster 1 & 2 are in-phase

Thruster 3 Side Right (GPIO10)

Thruster 4 Side Left (GPIO11)

Claw Servo 1 (GP12) ; Claw Servo 2 (GP13)

Software side :

PWM : 100Hz

PWM range : 1100us(Full Backward) <-> 1500us(Stop) <-> 1900us(Full Forward)
