import time
from adafruit_circuitplayground.express import cpx

def accel_demo(demo_count):
    while True:
        if cpx.switch:
            print("Slide switch off!")
            cpx.pixels.fill((0, 0, 0))
            continue
        else:
            R = 0
            G = 0
            B = 0
            x, y, z = cpx.acceleration
            print((x, y, z))
            if x:
                R = R + abs(int(x))
            if y:
                G = G + abs(int(y))
            if z:
                B = B + abs(int(z))
            print(R,G,B)
            cpx.pixels.fill((R, G, B))
            time.sleep(0.001)
            if cpx.button_a or cpx.button_b:
                while cpx.button_a or cpx.button_b: #debounce
                    time.sleep(0.1)
                return demo_count + 1