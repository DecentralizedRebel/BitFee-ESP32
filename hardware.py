print("Initializing platform Heltec Lora 32 WiFi")
from machine import Pin, SoftI2C
import os
# Download ssd1306 library if it is not already installed
try:
    if not '/lib' in os.listdir('/'):
        os.mkdir('/lib')
except OSError as e:
    if e.args[0] != 17:  # 17 is the error code for EEXIST
        raise e  # re-raise the exception if it's not EEXIST

# Check if ssd1306 driver is installed, install if not
if 'ssd1306.mpy' not in os.listdir('/lib'):
    print("Downloading ssd1306 driver")
    import mip
    mip.install('ssd1306')
else:
    print("ssd1306 driver already installed on device.")
import ssd1306

from time import sleep

def init_display():
    # Initialize 128*64 dot matrix OLED Display
    oled_width = 128
    oled_height = 64
    i2c_rst = Pin(16, Pin.OUT)
    i2c_rst.value(0)
    sleep(0.010)
    i2c_rst.value(1)
    i2c_scl = Pin(15, Pin.OUT, Pin.PULL_UP)
    i2c_sda = Pin(4, Pin.OUT, Pin.PULL_UP)
    i2c = SoftI2C(scl=i2c_scl, sda=i2c_sda)

    display = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
    return display

def display_print(display, text, line):
    if not isinstance(line, int):
        raise ValueError("Line number must be an integer")
    display.fill(0)
    display.text(text, 0, line * 10)
    display.show()
