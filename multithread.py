from machine import Pin
import _thread
import utime

red_led = Pin(20, mode = Pin.OUT, value = 0)
yellow_led = Pin(21, mode = Pin.OUT, value = 0)

def first_core_function():
    yellow_led.toggle()
    utime.sleep(5)
    yellow_led.toggle()
    utime.sleep(5)
    print("\n","Hello There ! i am the FIRST CORE","\n")
    
def second_core_function():
    while True:
        red_led.toggle()
        utime.sleep(1)
        red_led.toggle()
        utime.sleep(1)
        print("Hello There ! i am the SECOND CORE") 

_thread.start_new_thread(second_core_function, ())

while True:
    first_core_function()
