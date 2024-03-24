# turtleFish
Simple ROV with Touch Screen as interface
This is project intended to build a simple ROV with 4x3phase thruster.
Top side Hardware :
Touch screen Human Machine Interface (HMI)
RS485 module (Modulation)
Tether : 15m
Underwater Hardware :
RS485 module (Demodulation)
RP2040 ARM Cortex M0 MCU (Raspberry Pi Pico)
Servo Driver Break out board (https://www.waveshare.com/wiki/Pico-Servo-Driver)
4x(ESC + T200 Bluerobotic Thruster)

Software side :
PWM : 100Hz
PWM range : 1100us(Full Backward) <-> 1500us(Stop) <-> 1900us(Full Forward)
