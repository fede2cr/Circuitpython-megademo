import megademo_neopixels
import megademo_captouch

while True:
    if megademo_neopixels.rainbowCycleDemo:
        print('Rainbow Cycle Demo')
        megademo_neopixels.rainbow_cycle(.001)
    
    if megademo_neopixels.simpleCircleDemo:
        print('Simple Circle Demo')
        megademo_neopixels.simpleCircle(.05)

    if megademo_neopixels.rainbowDemo:
        print('Rainbow Demo')
        megademo_neopixels.rainbow(.001)


