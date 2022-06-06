import Adafruit_DHT
import time
def gettemp_and_hum():
# Set sensor type : Options are DHT11,DHT22 or AM2302
    sensor=Adafruit_DHT.DHT11
# Set GPIO sensor is connected to
    GPIO=22
# Use read_retry method. This will retry up to 15 times to
# get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(sensor, GPIO)
# Reading the DHT11 is very sensitive to timings and occasionally
# the Pi might fail to get a valid reading. So check if readings are valid.
    temp=round(temperature,2)
    hump=round(humidity,2)
    return temp,hump
