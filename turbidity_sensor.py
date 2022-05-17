import board
import busio
import time
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1115(i2c)

analog_channel = AnalogIn(ads, ADS.P0)


def read_turbidity():
    turbidity = analog_channel.voltage
    round(turbidity, 2)
    ntu = get_ntu(turbidity)
    return ntu


def get_ntu(voltage):
    ntu = -1120.4 * Math.sqrt(voltage) + 5742.3 * voltage - 4352.9
    return ntu


