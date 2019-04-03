from unittest import TestCase
from Student_Updating import add_grades_to_student
from Student import Student
from unittest.mock import patch
import io


class TestAdd_grades_to_student(TestCase):

    def setUp(self):
        self.testStudent1 = Student('Tommy', 'May', 'A01086435', True, ['90'])
        self.testStudent2 = Student('Another', 'Person', 'A01086436', True, [])

    @patch('builtins.input', side_effect=['80', '85', '95', 'done'])
    def test_add_grades_to_student(self, mock_input):
        students_list = [self.testStudent1]
        add_grades_to_student(0, students_list)
        actual_output = str(students_list[0])
        expected_output = '\nTommy May A01086435 True 90 80 85 95'
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=['done'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_non_integer_input(self, mock_output, mock_input):
        students_list = [self.testStudent1]
        add_grades_to_student(0, students_list)
        actual_output = mock_output.getvalue()
        expected_output = 'non integer grade entered, exiting edit\n\n' \
                          'All valid grades were added to the student\n'
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=['200'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_integer_above_100(self, mock_output, mock_input):
        students_list = [self.testStudent1]
        add_grades_to_student(0, students_list)
        actual_output = mock_output.getvalue()
        expected_output = 'You entered a grade below 0 or above 100, exiting edit\n\n' \
                          'All valid grades were added to the student\n'
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=['-20'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_integer_below_0(self, mock_output, mock_input):
        students_list = [self.testStudent1]
        add_grades_to_student(0, students_list)
        actual_output = mock_output.getvalue()
        expected_output = 'You entered a grade below 0 or above 100, exiting edit\n\n' \
                          'All valid grades were added to the student\n'
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=['10.5'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_float_input(self, mock_output, mock_input):
        students_list = [self.testStudent1]
        add_grades_to_student(0, students_list)
        actual_output = mock_output.getvalue()
        expected_output = 'non integer grade entered, exiting edit\n\n' \
                          'All valid grades were added to the student\n'
        self.assertEqual(expected_output, actual_output)
