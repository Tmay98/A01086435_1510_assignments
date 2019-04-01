from unittest import TestCase
from Student_Updating import find_student
from unittest.mock import patch


class TestFind_student_to_add_grades(TestCase):

    @patch('builtins.input', side_effect=['80', '90', 'done'])
    def test_find_student_to_add_grades(self, mock_input):
        open('students.txt', 'w').close()
        with open('students.txt', 'r+') as f_obj:
            lines = ['Tommy May A01086435 True 90\n']
            find_student(f_obj, lines, 'A01086435')
        with open('students.txt') as f_obj:
            actual_output = f_obj.read()
        expected_output = 'Tommy May A01086435 True 90 80 90\n'
        self.assertEqual(expected_output, actual_output)
