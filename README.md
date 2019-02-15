# MQTT-IoT
Here, I would implement popular IoT protocol "MQTT", to act both as publisher and subscriber for Upsquared board.

MQTT_LEDcontrol program would act as client in subscriber mode and it receives any incomming message from publisher. Once the correct message is received by subscriber, it would perform action by changing the GPIO pin value (which can control any appliance).

MQTT_read program would act as client in publisher mode and it would send sensor data to defined topic. Who ever is subscriber to defined topic,would recive the sensor value in json format.

For Server, who can act as subscriber (for MQTT_read) and publisher (for MQTT_LEDcontrol), I used an Android App "IoT MQTT Dashboard", available FREE on play store.
