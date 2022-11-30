# SPDX-FileCopyrightText: 2022 Pranab Salian
# SPDX-License-Identifier: GPL-3.0-or-later
# Soupara Tactile Macropad

import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

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

# Flash the LED once
with neopixel.NeoPixel(pixel_pin, num_pixels) as pixels:
    pixels.fill(GREEN)
    time.sleep(0.5)

# Set up the underlight
# Brightness can go from 0.1 to 1.0
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False)
pixels.fill(PURPLE)
pixels.show()

kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

# list of pins for keypad (skipping GP15 as it used to be funky, using it for Buzzer output)
pins = (
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11,
    board.GP12,
    board.GP13,
    board.GP14,
    board.GP16,
    board.GP17,
    board.GP18,
    board.GP19,
    board.GP20,
)

# GPIO 15 is made available on the PCB as BUZZ (intended for a Buzzer)
# but can also be used for other ideas like haptic feedback.

# GPIO 26 & 27 are also made available as I2C pins on the PCB

MEDIA = 1
KEY = 2

keymap = {
    (0): (KEY, (Keycode.GUI, Keycode.C)), # Mac Copy
    (1): (KEY, (Keycode.GUI, Keycode.V)), # Mac Paste
    (2): (KEY, [Keycode.THREE]),
    (3): (KEY, [Keycode.FOUR]),
    (4): (KEY, [Keycode.FIVE]),
    
    (5): (MEDIA, ConsumerControlCode.VOLUME_DECREMENT),
    (6): (MEDIA, ConsumerControlCode.VOLUME_INCREMENT),
    (7): (KEY, [Keycode.R]),
    (8): (KEY, [Keycode.G]),
    (9): (KEY, [Keycode.B]),
    
    (10): (KEY, [Keycode.UP_ARROW]),
    (11): (KEY, [Keycode.X]),  # plus key
    (12): (KEY, [Keycode.Y]),
    (13): (KEY, [Keycode.Z]),
    (14): (KEY, [Keycode.I]),
    
    (15): (KEY, [Keycode.O]),
    (16): (KEY, [Keycode.LEFT_ARROW]),
    (17): (KEY, [Keycode.DOWN_ARROW]),
    (18): (KEY, [Keycode.RIGHT_ARROW]),
    (19): (KEY, [Keycode.ALT]),

}

switches = []
for i in range(len(pins)):
    switch = DigitalInOut(pins[i])
    switch.direction = Direction.INPUT
    switch.pull = Pull.UP
    switches.append(switch)


switch_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while True:
    for button in range(20):
        if switch_state[button] == 0:
            if not switches[button].value:
                try:
                    if keymap[button][0] == KEY:
                        # This is a Key
                        kbd.press(*keymap[button][1])
                    else:
                        # This is a Media button
                        cc.send(keymap[button][1])
                except ValueError:  # deals with six key limit
                    pass
                switch_state[button] = 1

        if switch_state[button] == 1:
            if switches[button].value:
                try:
                    if keymap[button][0] == KEY:
                        kbd.release(*keymap[button][1])

                except ValueError:
                    pass
                switch_state[button] = 0

    time.sleep(0.01)  # debounce



