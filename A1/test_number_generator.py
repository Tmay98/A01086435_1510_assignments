from unittest import TestCase
import lotto


class TestNumber_generator(TestCase):
    def test_list_length(self):
        self.assertTrue(len(lotto.number_generator()) == 6)

    def test_numbers_in_range(self):
        self.assertTrue(0 <= lotto.number_generator()[0] < 50)
        self.assertTrue(0 <= lotto.number_generator()[1] < 50)
        self.assertTrue(0 <= lotto.number_generator()[2] < 50)
        self.assertTrue(0 <= lotto.number_generator()[3] < 50)
        self.assertTrue(0 <= lotto.number_generator()[4] < 50)
        self.assertTrue(0 <= lotto.number_generator()[5] < 50)

    def test_unique_numbers(self):
        self.assertTrue(lotto.number_generator()[0] != lotto.number_generator()[1] != lotto.number_generator()[2] !=
                        lotto.number_generator()[3] != lotto.number_generator()[4] != lotto.number_generator()[5])
