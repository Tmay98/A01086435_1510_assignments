from unittest import TestCase
import time_calculator


class TestTime_calculator(TestCase):
    def test_time_calculator(self):
        self.assertEqual(['days', 1, 'hours', 1, 'minutes', 42, 'seconds', 46], time_calculator.time_calculator(92566))

    def test_wrong_input(self):
        self.assertEqual(None, time_calculator.time_calculator(-5))

