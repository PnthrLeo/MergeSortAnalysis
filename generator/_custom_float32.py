from numpy import intc, float32, finfo


FLOAT32_MIN = float(finfo(float32).min)
FLOAT32_MAX = float(finfo(float32).max)


class CustomFloat32(float32):
    def __new__(self, num):
        return super().__new__(self, num)

    def __init__(self, num):
        self.effort = intc(0)

    def __eq__(self, num):
        self.effort += 1
        return super().__eq__(num)

    def __ne__(self, num):
        self.effort += 1
        return super().__ne__(num)

    def __lt__(self, num):
        self.effort += 1
        return super().__lt__(num)

    def __le__(self, num):
        self.effort += 1
        return super().__le__(num)

    def __gt__(self, num):
        self.effort += 1
        return super().__gt__(num)

    def __ge__(self, num):
        self.effort += 1
        return super().__ge__(num)


if __name__ == "__main__":
    a = CustomFloat32(2)
    b = CustomFloat32(5.1)
    print(type(a))
    print(a + b)
    print(b >= a)
    print(a.effort)
    print(b.effort)
