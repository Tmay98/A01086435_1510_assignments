from unittest import TestCase
from Student_Record import calculate_students_average


class TestCalculate_students_average(TestCase):

    def test_calculate_students_average(self):
        students_list = ['person one A01086435 True 60 70 80\n', 'person two A01086435 True 50 55 60\n',
                         'person one A01086435 True 90 95 100\n']
        actual_return = calculate_students_average(students_list)
        expected_return = [70.0, 55.0, 95.0]
        self.assertEqual(actual_return, expected_return)

    def test_students_with_no_grades(self):
        students_list = ['person one A01086435 True\n', 'person two A01086435 True\n',
                         'person one A01086435 True\n']
        actual_return = calculate_students_average(students_list)
        expected_return = []
        self.assertEqual(actual_return, expected_return)
