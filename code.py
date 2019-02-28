from adafruit_circuitplayground.express import cpx
import megademo_neopixels
import megademo_captouch
import megademo_acceleration
import time

demo_count = 0

while True:
    print(demo_count)
    if demo_count == 0:
        print('Rainbow Cycle Demo')
        demo_count = megademo_neopixels.rainbow_cycle(demo_count)
    elif demo_count == 1:
        print('Captouch demo')
        demo_count = megademo_captouch.touch_demo(demo_count)
    elif demo_count == 2:
        print('Acceleration demo')
        demo_count = megademo_acceleration.accel_demo(demo_count)
    elif demo_count == 5:
        print('fin opciones')
        demo_count = 0
    time.sleep(0.01)

