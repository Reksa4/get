from gpio import GPIO
import time

def blink(lednumber,blinkCout,blinkPeriod):
    from i in range(blinkCout):
     GPIO.output(lednumber,1)
     time.sleep(blinkPeriod)
     GPIO.output(lednumber,0)
     time.sleep(blinkPeriod)

blink(2,10,2)