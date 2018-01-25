import setup
from setup import RPL
import RoboPiLib as RPL

RPL.servoWrite(0,1000)
RPL.servoWrite(1,1000)

x = 1
while x == 1:
  RoboPi.analogRead(0)
  AnalogRead = RoboPi.analogRead(0)
  AnalogRead = int(AnalogRead)
  Dist = (500 * AnalogRead)/1024
  for Dist 
  
import RoboPiLib as RoboPi
