import time
import setup
from setup import RPL
import RoboPiLib as RPL
start = time.time()
elapsed = (time.time() - start)

global x
x = 2
global elapsed


while True:
    global x
    x = x % 2
    elapsed = int(elapsed)
    if elapsed == 3:
       RPL.servoWrite(0,0)
       x = x + 1
    if elapsed == 6:
       RPL.servoWrite(0,1000)
       x = x + 1

