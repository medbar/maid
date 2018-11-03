import RPi.GPIO as GPIO
import time
import sys


MOTORS = [[5, 7, 3],
          [13, 15, 11],
          [21, 23, 19],
          [31, 33, 29],
          [10, 12, 8]]
SEXSHIM = [35]

def setup():
    GPIO.setmode(GPIO.BOARD) #GPIO.setmode(GPIO.BOARD)
    for motor in MOTORS:
        for pin in motor:
            print(pin)
            GPIO.setup(pin, GPIO.OUT, initial=0)
    for shim in SEXSHIM:
        print(shim)
        GPIO.setup(shim, GPIO.OUT, initial=0)
        GPIO.output(shim,1)

def krutilo_levo(motor):
    GPIO.output(motor[0], 0)
    GPIO.output(motor[1], 1)
    GPIO.output(motor[2], 1)

def krutilo_pravo(motor):
    GPIO.output(motor[0], 1)
    GPIO.output(motor[1], 0)
    GPIO.output(motor[2], 1)



def apply_states(states):
    for i, curr_state in enumerate(states):
        if curr_state==-1:
            krutilo_levo(MOTORS[i])
        elif curr_state==0:
            GPIO.output(MOTORS[i][2], 0)
        elif curr_state==1:
            krutilo_pravo(MOTORS[i])

def clean_all_motors():
    for motor in MOTORS:
        GPIO.output(motor[2], 0)


def input_read():
    c = input()
    if len(c) == 1:
        t=1
    else:
        t=float(c[1:])
    return c[0], t


from pynput.keyboard import Key, Listener
manipulator_up = "uio"
manipulator_down = "jkl"
t=0.01
 
def on_press(key):
    print('{0} pressed'.format(key))
    states = [0, 0, 0, 0, 0]
    com= str(key).replace("'",'')
    print(com)
    print(com=="w")
    if com=='w':
        states[0] = 1
        states[1] = -1
    elif com=='a':
        states[0] = 1
        states[1] = 1
    elif com=='s':
        states[0] = -1
        states[1] = 1
    elif com=='d':
        states[0] = -1
        states[1] = -1

    for i in range(3):
        if com==manipulator_up[i]:
            states[2+i] = 1
        elif com==manipulator_down[i]:
            states[2 + i] = -1
    print(states) 
    apply_states(states)



def on_release(key):
    print('{0} release'.format(
        key))
    clean_all_motors()
    if key == Key.esc:
        # Stop listener
        return False



setup()
try:
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
except Exception as e:
    raise e
finally:
    GPIO.cleanup()
