import machine, utime
PWM_FREQ = 750
#define global pwm frequency

MOTOR_0 = machine.PWM(machine.Pin(0))
#define GPIO pin 0 as pwm pin
MOTOR_0.freq(PWM_FREQ)
#set defined pwm pin frequency

while(1):
    #main loop runs from 0->65025->0
    for duty in range(65025):
        MOTOR_0.duty_u16(duty)
        utime.sleep_us(100)

    for duty in range(65025,0,-1):
        MOTOR_0.duty_u16(duty)
        utime.sleep_us(100)
