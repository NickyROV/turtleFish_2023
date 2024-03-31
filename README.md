# turtleFish
This project was intended to build a simple 3 phase thruster driven ROV with Touch Screen as interface in 2 weeks time.

Task : Design & programming / Test / Sourcing / Assembly / Pilot run / Deployment

Top side Hardware : Touch screen Human Machine Interface (HMI)

Underwater Hardware : RP2040 ARM Cortex-M0 MCU (Pico) with Break out board

Communication protocol : UART in Hex via RS485

|Little Turtle Fish|Big Turtle Fish|
|---|---|
|4 x 3-phsae thrusters / 1 claw servo|6 x 3-phase thrusters / 2 claw servo|
|Tether : 15 m|Tether : 20 m|
|6 pairs of twisted cable of 0.75mm^2|6 pairs of twisted cable of 1.0mm^2| 
|2 x Fishing Camera|1 x Fishing Camera|

ESC -> PWM Freq 100Hz with range : 1100us(Full Backward) <-> 1500us(Stop) <-> 1900us(Full Forward)
