# Esp32Python

https://youtube.com/playlist?list=PL-3SnJmahyb5mQLq7RgG6HNIUMwXzgDy-&si=uQZo_DZwBbALXBjn

## FW

1. python.exe -m venv venv
1. pip install esptool
1. esptool.exe version
1. Connect device. Device manager -> ports -> check port number
1. erase flash: esptool --port COM6 erase_flash
1. install new fw to run micro python. download driver from here: https://micropython.org/download/ESP32_GENERIC/
1. write flash: esptool --chip esp32 --port COM6 write_flash -z 0x1000 C:\Temp\ESP32_GENERIC-20240602-v1.23.0.bin
1. MobaXterm -> Serial -> COM6. Speed 115200
1. click EN button on esp32 board
1. MobaXterm ->

> print('hello world')
> pin2 = machine.Pin(2, machine.Pin.OUT)
> pin2.on()
> pin2.off()

## Coding
