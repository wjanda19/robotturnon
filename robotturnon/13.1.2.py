import time
import setup
from setup import RPL
import RoboPiLib as RPL
start = time.time()


x = 2


while True:
    elapsed = (time.time() - start)
    x = 0
    elapsed = int(elapsed)
    if elapsed % 6 == 0:
       RPL.servoWrite(2,500)
       RPL.servoWrite(1,2000)
       x = x + 3
    if elapsed % 3 == 0:
       RPL.servoWrite(2,0)
       RPL.servoWrite(1,0)
       x = x + 6
 

