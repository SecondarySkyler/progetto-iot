from influxdb import InfluxDBClient
import time
import temp_sensor
import utils

SHUTDOWN = False

client = InfluxDBClient(host = 'localhost', port = 8086, user = 'python', password = 'pass')

data = []

while not SHUTDOWN:
   temp = temp_sensor.read_temp()
   data.append(utils.parse_json('Temperatura', 'gradi', 20))
   data.append(utils.parse_json('Torbidità', 'ntu', 0.5))
   data.append(utils.parse_json('pH', 'pH', 5))
   data.append(utils.parse_json('TDS', 'residuo fisso', 23))
   
   client.write_points(data, database = 'progetto', protocol = 'json')
   time.sleep(5)





