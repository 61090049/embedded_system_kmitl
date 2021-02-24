import machine, time, hcsr04

DIS_SENSOR = hcsr04.HCSR04(trigger_pin = 1, echo_pin = 0)
TIMER = machine.Timer()

def tim_handler(TIMER):
    print(DIS_SENSOR.distance_mm())
    
TIMER.init(period = 1000, mode=machine.Timer.PERIODIC, callback = tim_handler)

while True:  
    time.sleep_ms(100)
