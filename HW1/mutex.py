import pyb, mutex #import board lib, mutex lib
mutex = mutex.Mutex() #Creates an unlocked mutex object
data_ready = False

def callback(): # ISR
    global data_ready
    if mutex.test(): # Successfully acquiring mutext return true, else false
        # Can write to critical variable
        data_ready = True
        mutex.release()
    else:
        # Can't write to critical variable

while True: # main loop
    if data_ready:
        with mutex: # Try/Exception
            # main loop writing to critical variable
            data_ready = False

# The program's ISR test the main loop whether
# it was accesing the critical variable.
