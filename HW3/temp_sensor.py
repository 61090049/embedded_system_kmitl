import machine, time, onewire, ds18x20

TEMP_SENSOR = ds18x20.DS18X20(onewire.OneWire(machine.Pin(0)))
TIMER = machine.Timer()

def tim_handler(TIMER):
    TEMP_SENSOR.convert_temp()
    time.sleep_ms(750)
    print(TEMP_SENSOR.read_temp(TEMP_SENSOR.scan()[0]))

TIMER.init(period = 1000, mode=machine.Timer.PERIODIC, callback = tim_handler)

while True:  
    time.sleep_ms(100)
