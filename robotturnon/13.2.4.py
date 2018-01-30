import time
import setup
from setup import RPL
import post_to_web as PTW # see post_to_web.py for instructions

sensor_pin = 1
RPL.pinMode(sensor_pin,RPL.INPUT)

#def testing():
 # RPL.servoWrite(0,2000)
 # RPL.servoWrite(1,1000)
  #time.sleep()

while True:
  PTW.state['d1'] = RPL.digitalRead(sensor_pin)
  PTW.post()

  import RoboPiLib as RPL
  import setup
  RPL.servoWrite(0,1000)
  RPL.servoWrite(1,2000)
  if RPL.digitalRead(sensor_pin) == 0:
     import RoboPiLib as RPL
     import setup
     start = time.time()
     RPL.servoWrite(0,1501)
     RPL.servoWrite(1,1501)
     elapsed = (time.time() - start)
     elapsed = int(elapsed)
     print elapsed
     if elapsed == 3:
       RPL.servoWrite (0,0)
       RPL.servoWrite (1,0)
