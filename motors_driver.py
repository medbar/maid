import RPi.GPIO as GPIO


class MotorsDriver():
    def __init__(self):
        MOTORS = [[5, 7, 3],
                  [13, 15, 11],
                  [21, 23, 19],
                  [31, 33, 29],
                  [10, 12, 8]]
        SHIM = [35]

    def setup(self):
        GPIO.setmode(GPIO.BOARD) #GPIO.setmode(GPIO.BOARD)
        for motor in self.MOTORS:
            for pin in motor:
                print(pin)
                GPIO.setup(pin, GPIO.OUT, initial=0)
        for shim in self.SHIM:
            print(shim)
            GPIO.setup(shim, GPIO.OUT, initial=0)
            GPIO.output(shim, 1)

    def left(self,motor):
        GPIO.output(motor[0], 0)
        GPIO.output(motor[1], 1)
        GPIO.output(motor[2], 1)

    def right(self, motor):
        GPIO.output(motor[0], 1)
        GPIO.output(motor[1], 0)
        GPIO.output(motor[2], 1)

    def apply_states(self, states):
        for i, curr_state in enumerate(states):
            if curr_state < 0:
                self.left(self.MOTORS[i])
            elif curr_state == 0:
                GPIO.output(self.MOTORS[i][2], 0)
            elif curr_state > 0:
                self.right(self.MOTORS[i])

    def clean_all_motors(self):
        for motor in self.MOTORS:
            GPIO.output(motor[2], 0)