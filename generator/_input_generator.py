import random
from ._custom_float32 import CustomFloat32, FLOAT32_MIN, FLOAT32_MAX


class InputGenerator:
    def __init__(self, input_size):
        self.input_size = input_size

    def __call__(self):
        arr = []
        for i in range(self.input_size):
            num = random.uniform(FLOAT32_MIN, FLOAT32_MAX)
            num = CustomFloat32(num)
            arr.append(num)
        return arr
