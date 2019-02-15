import mraa
import os
import time
import sys
import paho.mqtt.client as mqtt
import json

INTERVAL=2
sensor_data = {'temperature': 0, 'humidity': 0}
next_reading = time.time()
client = mqtt.Client()

client.connect("test.mosquitto.org", 1883, 60)

client.loop_start()

try:
    while True:
        mraa.addSubplatform(mraa.GROVEPI, "0")
        temp=mraa.Aio(512)
        sensor=temp.read()
        hum=mraa.Aio(513)
        humidity=temp.read()
	print("Time: {}, Temperature: {},Humidity: {}" .format(next_reading, sensor)
        sensor_data['temperature'] = sensor
        sensor_data['humidity'] = humidity

        # Sending humidity and temperature data to ThingsBoard
        client.publish('MQTTUP2', json.dumps(sensor_data))

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
		time.sleep(sleep_time)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()
