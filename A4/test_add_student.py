from unittest import TestCase
from Student_Creation import add_student
from unittest.mock import patch
import io


class TestAdd_student(TestCase):

    @patch('builtins.input', side_effect=['tommy may A01086435'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_student_not_enough_input(self, mock_stdout, mock_input):
        add_student()
        actual_output = mock_stdout.getvalue()
        expected_output = 'You did not enter all required fields for the student' \
                          ' (FirstName, LastName, Student#, standing)\n\n'
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=['34fl; may A01086435 True'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_student_incorrect_first_name(self, mock_stdout, mock_input):
        add_student()
        actual_output = mock_stdout.getvalue()
        expected_output = 'You entered an incorrect name\n'
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=['tommy ;3[2f A01086435 True'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_student_incorrect_last_name(self, mock_stdout, mock_input):
        add_student()
        actual_output = mock_stdout.getvalue()
        expected_output = 'You entered an incorrect name\n'
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=['tommy may A013gvf6435 True'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_student_incorrect_student_number(self, mock_stdout, mock_input):
        add_student()
        actual_output = mock_stdout.getvalue()
        expected_output = 'You entered an incorrect student number\n'
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=['tommy may A01086435 True 50 30 40'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_student_with_grades(self, mock_stdout, mock_input):
        add_student()
        actual_output = mock_stdout.getvalue()
        expected_output = 'student added to file\n'
        self.assertEqual(expected_output, actual_output)
