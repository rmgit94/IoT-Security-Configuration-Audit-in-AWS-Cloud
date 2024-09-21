import time

def customCallback(client,userdata,message):
    print("callback came...")
    print(message.payload)

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

myMQTTClient = AWSIoTMQTTClient("dojodevice1")
myMQTTClient.configureEndpoint("a2wce5ar31lyfa-ats.iot.us-east-1.amazonaws.com", 8883)
myMQTTClient.configureCredentials("./AmazonRootCA1.pem","./dce1c1cb14e398a72ba2c98a0db761f8863948bc343e9416ced435f0758a7860-private.pem.key", "./dce1c1cb14e398a72ba2c98a0db761f8863948bc343e9416ced435f0758a7860-certificate.pem.txt")

myMQTTClient.connect()
print("Client Connected")

myMQTTClient.subscribe("general/outbound", 1, customCallback)
print('waiting for the callback. Click to conntinue...')
x = input()

myMQTTClient.unsubscribe("general/outbound")
print("Client unsubscribed") 


myMQTTClient.disconnect()
print("Client Disconnected")