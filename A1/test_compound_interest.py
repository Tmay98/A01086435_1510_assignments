from unittest import TestCase
import compound_interest


class TestCompound_interest(TestCase):
    def test_compound_interest(self):
        self.assertEqual(268.5063838389963, compound_interest.compound_interest(100, 0.10, 4, 10))

    def test_no_interest(self):
        self.assertEqual(100, compound_interest.compound_interest(100,0,2,4))
