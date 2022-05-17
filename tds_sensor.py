import board
import busio
import time
import math
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1115(i2c)

analog_channel = AnalogIn(ads, ADS.P2)


def read_tds():
    tds_voltage = analog_channel.voltage
    tds_voltage = round(tds, 2)
    ppm = get_ppm(tds_voltage)
    return ppm



def get_ppm(voltage):
    ppm = (133.42 / pow(voltage, 3) - 255.86 * pow(voltage, 2) + 857.39 * voltage) * 0.5
    ppm = round(ppm, 2)
    return ppm
