from gpio import GPIO
import time

def runninDark(count,period):
    x = 0
    GPIO.output(0,1)
    GPIO.output(1,1)
    GPIO.output(2,1)
    GPIO.output(3,1)
    GPIO.output(4,1)
    GPIO.output(5,1)
    GPIO.output(6,1)
    GPIO.output(7,1)
    for i in range(count):
        GPIO.output(x,0)
        time.sleep(period)
        x += 1
        GPIO.output(x-1,1)
        if x > 7:
            x = 0
runninDark(100,1)