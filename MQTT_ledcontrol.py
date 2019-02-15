import paho.mqtt.client as mqtt
import mraa


led1 = mraa.Gpio(2)    
led2 = mraa.Gpio(13)   
led1.dir(mraa.DIR_OUT) 
led2.dir(mraa.DIR_OUT)

def on_connect(client, userdata, flags, rc):
    print("Connected to broker. Return of connection: "+str(rc))


    client.subscribe("/MQTTLED/#")

# Callback - when a message is received
def on_message(client, userdata, msg):
        print("Topic: "+msg.topic+" - Message Received: "+str(msg.payload))

        if (str(msg.payload) == "ONLED1"):
                led1.write(1)
                return 0

        if (str(msg.payload) == "ONLED2"):
                led2.write(1)
                return 0

        if (str(msg.payload) == "OFFLED1"):
                led1.write(0)
                return 0

        if (str(msg.payload) == "OFFLED2"):
                led2.write(0)
	  return 0


#main program
client = mqtt.Client()
client.on_connect = on_connect   # configure callback (from when the connection$
client.on_message = on_message   # set callback (from when a message is receive$

client.connect("test.mosquitto.org", 1883, 60)
# tries to connect to the broker on port 1883 (the parameter '60' is the
# keepalive time). In that case, if no message is transmitted within 60
# seconds, you have pinged the broker from time to time (to keep the
# connection active

# Endless loop waiting to receive messages. .
client.loop_forever()
