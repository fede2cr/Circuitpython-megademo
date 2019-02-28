import time
from adafruit_circuitplayground.express import cpx

def touch_demo(demo_count):
    while True:
        if cpx.touch_A1:
            cpx.start_tone(330)
            cpx.pixels[6] = ((255,0,0))
            print("Touched A1!")
        elif cpx.touch_A2:
            cpx.start_tone(394)
            cpx.pixels[8] = ((255,0,0))
            print("Touched A2!")
        elif cpx.touch_A3:
            cpx.start_tone(294)
            cpx.pixels[9] = ((255,0,0))
            print("Touched A3!")
        elif cpx.touch_A4:
            cpx.start_tone(262)
            cpx.pixels[0] = ((255,0,0))
            print("Touched A4!")
        elif cpx.touch_A5:
            cpx.start_tone(440)
            cpx.pixels[1] = ((255,0,0))
            print("Touched A5!")
        elif cpx.touch_A6:
            cpx.start_tone(494)
            cpx.pixels[8] = ((255,0,0))
            print("Touched A6!")
        elif cpx.touch_A7:
            cpx.start_tone(523)
            cpx.pixels[3] = ((255,0,0))
            print("Touched A7!")
        elif cpx.button_a or cpx.button_b:
            while cpx.button_a or cpx.button_b: #debounce
                time.sleep(0.1)
            demo_count = demo_count + 1
            return demo_count
        else:
            cpx.stop_tone()
            cpx.pixels.fill((0, 0, 0))