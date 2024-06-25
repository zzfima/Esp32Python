from machine import Pin
import time

pin2 = Pin(2, Pin.OUT)
def blink():
    lap = 0
    while lap < 5:
        pin2.on()
        time.sleep(1)
        pin2.off()
        time.sleep(1)
        lap += 1

