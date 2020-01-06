from twython import Twython
from gpiozero import MotionSensor

from auth import (
  consumer_key,
  consumer_secret,
  access_token,
  access_token_secret
)

pir = MotionSensor(4)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

pir.wait_for_motion()
message = "Motion Detected!"
twitter.update_status(status=message)
print("Tweeted: %s" % message)
