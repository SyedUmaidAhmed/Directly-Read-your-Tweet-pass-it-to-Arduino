import serial
import time
from twython import TwythonStreamer
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

arduinoSerialData = serial.Serial('/dev/ttyUSB0',9600)

#arduinoSerialData = serial.Serial('/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_7573530303235181E1F0-if00',9600)


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            tweet = data['text']
            print(tweet)
            arduinoSerialData.write(tweet)

stream = MyStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

stream.statuses.filter(follow='809074068075020288')


# If you want your twitter ID number
# http://gettwitterid.com


#arduinoSerialData.open()
