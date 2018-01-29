import setup
from setup import RPL
import RoboPiLib as RoboPi

#RPL.servoWrite(0,1000)
#RPL.servoWrite(1,1000)

x = 1
while x == 1:
  RoboPi.analogRead(1)
  AnalogRead = RoboPi.analogRead(1)
  AnalogRead = int(AnalogRead)
  print AnalogRead
  
  
 # Dist = (500 * AnalogRead)/1024
#  print Dist
  
#import RoboPiLib as RoboPi
