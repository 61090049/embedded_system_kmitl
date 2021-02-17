import machine, utime

LED = machine.Pin(25, machine.Pin.OUT)
#Set onboard led as pinout
SENSOR_LIQUID_LEVEL = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)
#Set GPIO pin 0 as pin in

def irq_handler(some_pin):
    #define interrupt handler actions
    LED.value(1)

SENSOR_LIQUID_LEVEL.irq(trigger=machine.Pin.IRQ_RISING, handler=irq_handler)
#register interrupt handler to corresponding pin
LED.value(0)
#init led to off state
while(1):
    #main loop with delay
    utime.sleep_ms(200)