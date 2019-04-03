from unittest import TestCase
from Student_Updating import check_valid_student_number


class TestCheck_valid_student_number(TestCase):
    def test_check_valid_student_number(self):
        self.assertTrue(check_valid_student_number('A01086435'))

    def test_student_number_too_long(self):
        with self.assertRaises(ValueError):
            check_valid_student_number('A01086435555')

    def test_student_number_too_short(self):
        with self.assertRaises(ValueError):
            check_valid_student_number('A055')

    def test_first_letter_not_A(self):
        with self.assertRaises(ValueError):
            check_valid_student_number('B01086435555')

    def test_incorrect_format(self):
        with self.assertRaises(ValueError):
            check_valid_student_number('A0108g4h3')
