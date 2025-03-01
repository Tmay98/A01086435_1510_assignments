from unittest import TestCase
from unittest.mock import patch
from Student_Updating import file_delete_student
from Student import Student
import os


class TestFile_delete_student(TestCase):

    def setUp(self):
        self.testStudent1 = Student('Tommy', 'May', 'A01086435', True, ['90'])
        self.testStudent2 = Student('Another', 'Person', 'A01086436', True, [])

    @patch('builtins.input', side_effect=['A01086435'])
    def test_file_delete_student(self, mock_input):
        expected_output = '\nAnother Person A01086436 True '
        with open('students.txt', 'w') as f_obj:
            f_obj.write(str(self.testStudent1))
            f_obj.write(str(self.testStudent2))
        students_list = [self.testStudent1, self.testStudent2]
        file_delete_student(students_list)
        with open('students.txt', 'r') as f_obj:
            actual_output = f_obj.read()
        self.assertEqual(expected_output, actual_output)
        os.remove('students.txt')

    @patch('builtins.input', side_effect=['A59402346'])
    def test_student_not_found_returns_False(self, mock_input):
        with open('students.txt', 'w') as f_obj:
            f_obj.write(str(self.testStudent1))
            f_obj.write(str(self.testStudent2))
            students_list = [self.testStudent1, self.testStudent2]
        self.assertFalse(file_delete_student(students_list))
        os.remove('students.txt')

    @patch('builtins.input', side_effect=['A01086435'])
    def test_student_found_returns_True(self, mock_input):
        expected_output = '\nAnother Person A01086436 True '
        with open('students.txt', 'w') as f_obj:
            f_obj.write(str(self.testStudent1))
            f_obj.write(str(self.testStudent2))
            students_list = [self.testStudent1, self.testStudent2]
        self.assertTrue(file_delete_student(students_list))
        os.remove('students.txt')

    @patch('builtins.input', side_effect=['wefwefas'])
    def test_incorrect_student_number(self, mock_input):
        students_list = [self.testStudent1, self.testStudent2]
        self.assertFalse(file_delete_student(students_list))


