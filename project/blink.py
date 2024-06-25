from machine import Pin
import time

pin2 = Pin(2, Pin.OUT)
def blink():
    lap = 0
    while lap < 5:
        pin2.on()
        time.sleep(0.2)
        pin2.off()
        time.sleep(0.2)
        lap += 1

