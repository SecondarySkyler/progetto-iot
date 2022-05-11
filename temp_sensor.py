import os
import glob #usefull for search directory with jolly * character

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

BASE_DIR = '/sys/bus/w1/devices/'
SENSOR_DIR = glob.glob(BASE_DIR + '28*')[0]
FULLPATH = os.path.join(BASE_DIR, SENSOR_DIR)
FILE = FULLPATH + '/temperature'


def read_temp():
    file = open(FILE, 'r')
    lines = file.readlines()
    file.close()
    return lines

print(read_temp())

