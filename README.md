# turtleFish
This project was intended to build a simple 3 phase thruster driven ROV with Touch Screen as interface in 2 weeks time.

Task : Design & programming / Test / Sourcing / Assembly / Pilot run / Deployment

Top side Hardware : Touch screen Human Machine Interface (HMI)

Underwater Hardware : RP2040 ARM Cortex M0 MCU (Raspberry Pi Pico) with

Servo Driver Break out board (https://www.waveshare.com/wiki/Pico-Servo-Driver)

|Little Fish|Big Fish|
|---|---|
|4 x 3-phsae thrusters / 1 claw servo|6 x 3-phase thrusters / 2 claw servo|
|Tether : 15 m|Tether : 20 m|
|6 pairs of twisted cable of 0.75mm^2|6 pairs of twisted cable of 1.0mm^2| 
|2 x Fishing Camera|1 x Fishing Camera|

PWM Frequency : 100Hz

PWM range : 1100us(Full Backward) <-> 1500us(Stop) <-> 1900us(Full Forward)
