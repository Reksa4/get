from gpio import GPIO
import time

def runningLight(count,period):
    x = 0
    for i in range(count):
        GPIO.output(x,1)
        time.sleep(period)
        x += 1
        GPIO.output(x-1,0)
        if x >7:
            x = 0

runningLight(20,1)   