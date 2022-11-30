# SPDX-FileCopyrightText: 2022 Pranab Salian
# SPDX-License-Identifier: GPL-3.0-or-later
# Soupara Tactile Macropad

import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

print("---Soupara Tactile Macropad---")

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
led.value = True

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)

pixel_pin = board.GP22
num_pixels = 1

with neopixel.NeoPixel(pixel_pin, num_pixels) as pixels:
    pixels.fill(GREEN)
    time.sleep(2)
    
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False)
pixels.fill(WHITE)
pixels.show()
print("RGB Testing")

while True:
    for color in [RED, YELLOW, GREEN, CYAN, BLUE, PURPLE]:
        pixels.fill(color)
        pixels.show()
        # Increase or decrease to change the speed of the solid color change.
        time.sleep(1)
    
    pixels.fill(GREEN)
    pixels.show()
    time.sleep(1)
    pixels.fill(BLUE)
    pixels.show()
    time.sleep(1)
