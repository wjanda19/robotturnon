import time
import setup
from setup import RPL
import RoboPiLib as RPL
RPL.servoWrite(0,1000)
start = time.time()

elapsed = (time.time() - start)
if elapsed % 3 == 0:
    if elapsed == 3:
        import RoboPiLib as RPL
        import setup
        RPL.servoWrite(0,0)
