# Needed for analog readings
import time
import board
from analogio import AnalogIn

import struct

# Needed for RFM9X
import digitalio
#import board
import busio
import adafruit_rfm9x

# Setup the radio
cs = digitalio.DigitalInOut(board.RFM9X_CS)
reset = digitalio.DigitalInOut(board.RFM9X_RST)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)

# Pin mapping
analog_X = AnalogIn(board.A2)
analog_Y = AnalogIn(board.A3)
analog_trigger = AnalogIn(board.A4)

# Read analog pins
def get_analog(pin):
    return (pin.value)

def get_trigger(pin):
    if (pin.value > 60000):
        return True
    else:
        return False

while True:
    #rfm9x_sentence = (get_analog(analog_X),get_analog(analog_Y),get_trigger(analog_trigger))
    rfm9x_sentence = struct.pack('>HHb',get_analog(analog_X), get_analog(analog_Y), get_trigger(analog_trigger))
    rfm9x.send('Hello world!')
    rfm9x.send(rfm9x_sentence)
    print(rfm9x_sentence)
    time.sleep(1)
    #time.sleep(0.1)
