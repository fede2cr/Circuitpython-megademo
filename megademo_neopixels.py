import time
from adafruit_circuitplayground.express import cpx

cpx.pixels.brightness = 0.1
cpx.pixels.fill((0, 0, 0))

simpleCircleDemo = 1

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 85:
        return (int(pos * 3), int(255 - (pos * 3)), 0)
    elif pos < 170:
        pos -= 85
        return (int(255 - (pos * 3)), 0, int(pos * 3))
    else:
        pos -= 170
        return (0, int(pos * 3), int(255 - pos * 3))


def rainbow_cycle(demo_count):
    for j in range(255):
        for i in range(len(cpx.pixels)):
            idx = int((i * 256 / len(cpx.pixels)) + j * 10)
            cpx.pixels[i] = wheel(idx & 255)
        if cpx.button_a or cpx.button_b:
            while cpx.button_a or cpx.button_b: #debounce
                time.sleep(0.1)
            cpx.pixels.fill((0, 0, 0))
            return demo_count + 1
        else:
            time.sleep(0.01)