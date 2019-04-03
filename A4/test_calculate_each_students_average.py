from unittest import TestCase
from Student_Read_Write import calculate_each_students_average
from Student import Student

class TestCalculate_each_students_average(TestCase):

    def setUp(self):
        self.testStudent1 = Student('Tommy', 'May', 'A01086435', True, ['60', '70', '80'])
        self.testStudent2 = Student('Another', 'Person', 'A01086436', True, ['50', '55', '60'])
        self.testStudent3 = Student('Tommy', 'May', 'A01086435', True, [])
        self.testStudent4 = Student('Another', 'Person', 'A01086436', True, [])

    def test_calculate_students_average(self):
        students_list = [self.testStudent1, self.testStudent2]
        actual_return = calculate_each_students_average(students_list)
        expected_return = [70.0, 55.0]
        self.assertEqual(actual_return, expected_return)

    def test_students_with_no_grades(self):
        students_list = [self.testStudent3, self.testStudent4]
        actual_return = calculate_each_students_average(students_list)
        expected_return = []
        self.assertEqual(actual_return, expected_return)
