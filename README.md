# Circuitpython-megademo
A CircuitPython port of the CircuitPlayground megademo

## What is this?

CircuitPlayground boards from Adafruit are great... amazing. Even better than an Arduino UNO, you can program it using CircuitPython, without installing any software... But, to show it the wonderful hardware to someone, you have to upload the Arduino sketch called mega_demo.

## Megademo

Mega_demo is a demonstration code made by Tony DiCola to show of as many of the CircuitPlayground hardware as possible, with the available resources on the atmega328p chip from the first version of the Playgrounds.

This bit is taken from the original code, in the library for Arduino IDE.

```
// - NeoPixel color rainbow cycle
//   This animates all 10 neopixels with a rainbow cycle.  Changing the mode
//   changes the speed of animation.
// - Volume level meter
//   This uses the microphone to display a volume level meter.  The louder the
//   volume the more lights light up (and a peak level dot animates back down).
//   Changing mode changes the sensitivity from medium to very high to very low
//   and back to medium again (3 levels).
// - Capacitive touch instrument
//   This uses the capacitive touch pads (0, 1, 2, 3, 6, 9, 10, 12) and lights up
//   a nearby pixel when a pad is touched.  Pressing the mode toggles between
//   playing a different tone for each pad too (8 notes total covering the basic
//   C4 scale).
// - Accelerometer tilt demo
//   This lights up all the pixels to a color between blue and red depending on
//   the value of the accelerometer.  Try tilting the board around axes to see
//   how it behaves.  Pressing mode toggles between the X, Y, Z axis as the one
//   under measurements (starts with X axis).
// - Temperature & light sensor demo
//   The left half of the pixels light up blue proportional to the temperature
//   of the thermistor, and the right half of the pixels light up red proportional
//   to the light sensor.  Pressing mode toggles between small, medium, and big
//   ranges of measurements for each sensor.
```

## How to use?

Just copy this files to your board. Remember to add the CircuitPython Bundle library.

### Why?

- To keep the work of the great Tony DiCola alive
- To show a Playground to a new user, with CircuitPython
- Made with love and rainbows for the CircuitPython Community and Adafruit.

### Progress

All of the Arduino mega_demo code is being ported into individual files, which will later on be stiched into a single demo with chanse to select via the buttons.

--
*Alvaro Figueroa*

[Greencore Solutions](https://www.greencore.co.cr)

