from unittest import TestCase
from Student_Updating import check_if_student_in_file
from Student import Student
from unittest.mock import patch


class TestCheck_if_student_in_file(TestCase):
    def setUp(self):
        self.testStudent1 = Student('Tommy', 'May', 'A01086435', True, ['90'])
        self.testStudent2 = Student('Another', 'Person', 'A01086436', True, [])

    @patch('builtins.input', side_effect=['A59402346'])
    def test_student_not_found_returns_False(self, mock_input):
        with open('students.txt', 'w') as f_obj:
            f_obj.write(str(self.testStudent1))
            f_obj.write(str(self.testStudent2))
        self.assertFalse(check_if_student_in_file('A01086439'))

    @patch('builtins.input', side_effect=['A59402346'])
    def test_student_found(self, mock_input):
        with open('students.txt', 'w') as f_obj:
            f_obj.write(str(self.testStudent1))
            f_obj.write(str(self.testStudent2))
        self.assertTrue(check_if_student_in_file('A01086435'))
