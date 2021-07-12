"""
calc.py contains the Calculator class for testing examples.
"""


class Calculator(object):
    def __init__(self):
        self._last_answer = 0.0

    @property
    def last_answer(self):
        return self._last_answer

    def add(self, a, b):
        self._last_answer = a + b
        return self.last_answer

    def subtract(self, a, b):
        self._last_answer = a - b
        return self.last_answer

    def multiply(self, a, b):
        self._last_answer = a * b
        return self.last_answer

    def divide(self, a, b):
        # automatically raises ZeroDivisionError
        if a<100 and a>0 and b!=0:
            self._last_answer = a * 1.0 / b
        else:
            print('Be careful, a and b values are not compliant')
        return self.last_answer

    def maximum(self, a, b):
        self._last_answer = a if a >= b else b
        return self.last_answer

    def minimum(self, a, b):
        self._last_answer = a if a <= b else b
        return self.last_answer
