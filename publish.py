from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import sys

myMQTTClient = AWSIoTMQTTClient("dojodevice1")

myMQTTClient.configureEndpoint("a2wce5ar31lyfa-ats.iot.us-east-1.amazonaws.com", 8883)
myMQTTClient.configureCredentials("./AmazonRootCA1.pem","./dce1c1cb14e398a72ba2c98a0db761f8863948bc343e9416ced435f0758a7860-private.pem.key", "./dce1c1cb14e398a72ba2c98a0db761f8863948bc343e9416ced435f0758a7860-certificate.pem.txt")

myMQTTClient.connect()
print("Client Connected")

msg = "User heartbeat collected";
topic = "general/inbound"
myMQTTClient.publish(topic, msg, 0)  
print("Message Sent")

myMQTTClient.disconnect()
print("Client Disconnected")