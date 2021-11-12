import time
from adafruit_motorkit import MotorKit
from encoder import Encoder
import board

# NEEDS TO BE CALCULATED!
COUNT_TO_THROTTLE = 1
THROTTLE_TO_COUNT = 1


class Motor:

    def __init__(self):
        self.kit = MotorKit(i2c=board.I2C())
        self.actual_speed = 0
        self.prev_error = 0

    def __repr__(self):
        return str(self.actual_speed)

    def run(self, speed, encoder):
        throttle_speed = speed * COUNT_TO_THROTTLE
        self.kit.motor1.throttle = throttle_speed
        time.sleep(0.002)
        self.actual_speed = self.get_speed(encoder, 0.002)
        self.brake()

        return self.actual_speed

    def brake(self):
        # STEADY/GRADUAL STOP
        self.kit.motor1.throttle = None
        time.sleep(0.5)
        self.kit.motor1.throttle = 0

    def get_speed(self, encoder, time_interval):
        actual_speed = encoder.count() / time_interval
        return actual_speed
