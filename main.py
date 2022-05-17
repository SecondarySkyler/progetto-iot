from influxdb import InfluxDBClient
import time
import temp_sensor
import turbidity_sensor
import tds_sensor
import utils

SHUTDOWN = False

client = InfluxDBClient(host = 'localhost', port = 8086, username = 'python', password = 'pass')

data = []

while not SHUTDOWN:
   temp = temp_sensor.read_temp()
   turb = turbidity_sensor.read_turbidity()
   tds = tds_sensor.read_tds()
   data.append(utils.parse_json('Temperatura', 'gradi', temp))
   data.append(utils.parse_json('Torbidita', 'ntu', turb))
   data.append(utils.parse_json('pH', 'pH', 5))
   data.append(utils.parse_json('TDS', 'residuo fisso', tds))
   
   client.write_points(data, database = 'progetto', protocol = 'json')
   time.sleep(5)





