import machine, utime

LED = machine.Pin(25, machine.Pin.OUT)
#Set onboard led as pinout
SENSOR_PIR = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)
#Set GPIO pin 0 as pin in

def irq_handler(some_pin):
    #define interrupt handler actions
    LED.value(1)

SENSOR_PIR.irq(trigger=machine.Pin.IRQ_RISING, handler=irq_handler)
#register interrupt handler to pin
LED.value(0)
#make sure the led is off
while(1):
    #main loop with delay
    utime.sleep_ms(500)