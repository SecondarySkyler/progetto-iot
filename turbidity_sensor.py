import board
import busio
import time
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1115(i2c)

analog_channel = AnalogIn(ads, ADS.P0)

while True:
    print(analog_channel.value, analog_channel.voltage)
    time.sleep(3)

