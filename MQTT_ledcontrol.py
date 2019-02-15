import paho.mqtt.client as mqtt
import mraa

mraa.addSubplatform(mraa.GROVEPI, "0")
led1 = mraa.Gpio(516) 
led2 = mraa.Gpio(517)
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
client.on_connect = on_connect   
client.on_message = on_message   

client.connect("test.mosquitto.org", 1883, 60)


# Endless loop waiting to receive messages. .
client.loop_forever()
