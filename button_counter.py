from machine import Pin
from utime import sleep

x = 0

button = Pin(14,Pin.IN,Pin.PULL_DOWN)

def button_clicked(pin):
    if pin.value() == 1:
        sleep(0.1)
        while pin.value() == 1:
          pass
        return True
    else:
        return False


while True:
    if button_clicked(button):
        x = x+1
        print(x)