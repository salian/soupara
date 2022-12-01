# PCB Assembly

## BOM

To build the macropad you need 

| **Component** | **Qty** | **Price ₹** |
| :-------- |:---:|:---------|
| Raspberry Pi Pico | 1 | 320/- |
| 12x12x7.3mm Tactile Push Button Switch | 20 | 120/- |
| Keycaps (round or square for tactile switches) | 20 | 80/- |

Optionally you could also add

| **Optional Addons** | | |
| :-------- |:---:|:---------|
| Buzzer | 1 | 10/- |
| I2C display | 1 | 250/- |
| 1.27mm 1×40 Pin Male Single Row Header Strip | 1 | 20/- |
| Shorting Jumper | 1 | 2/- |
| WS2812B 5050 Addressable RGB LED | 1 | 5/- |

## Equipment

- Soldering Iron with fine tip
- Flux

## Assembly

#### Step I (optional)
- Start with soldering the (optional) WS2812B 5050 Addressable RGB LED on the underside of the PCB. 

#### Step II
- Solder on the Raspberry Pi Pico.

#### Step III (optional, if you soldered the RGB LED) 

- Plug the Raspberrry Pi Pico into your PC.
- Save the [latest Circuitpython UF2](https://circuitpython.org/board/raspberry_pi_pico/) file to the Pico.
- Upload the test [code.py](../firmware/circuitpython/rgb-led-test) to check if your LED was soldered on properly. The LED will cycle through various colours.

#### Step IV

- Solder the switches.
- Optionally break off a header strip into a 3-pin and 4-pin piece, and solder them into the jumper and I2C display holes on the PCB. This is needed only if you want to add in I2C peripherals. 

#### Step V

- Plug the Raspberrry Pi Pico into your PC
- Upload the sample [code.py](../firmware/circuitpython/sample) to the Pico. 
- [Download](https://circuitpython.org/libraries) the adafruit_hid folder and neopixel.mpy, adafruit_pixelbuf.mpy and neopixel_spi.mpy libraries and save to /lib on the Pico
- Edit code.py using Thonny or an editor of your choice, to customize the keys' functionality.
- Follow the assembly instructions for the case of your choice.
