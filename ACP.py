import RPi.GPIO as GPIO
import time

bit_depth = 8
def bin_convert(n):
    N = bit_depth - 1
    p = 0
    X = []
    while N > 0:
        p = int(n/2**N)
        if p == 1:
            X.append(1)
            n-=2**N
        else:
            X.append(0)
        N-=1
    X.append(n)
    return X
def dac_data(data):
    for i in range(0,bit_depth):
        GPIO.output(D[i], N[i])
def adc_procedure():
    for j in range(0,2**bit_depth):
        dac_data(bin_convert(j))
        time.sleep(0.1)

        m = (3.3 * j)/256
        print(j,'   ',m)
        if GPIO.input(4) == 0:
            print(j)
            break
    return j

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(1,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(4,GPIO.IN)

D=[21,20,16,12,1,7,8,25]


