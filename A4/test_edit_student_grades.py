from unittest import TestCase
from Student_Updating import edit_student_grades
from unittest.mock import patch
from Student import Student
import os


class TestEdit_student_grades(TestCase):

    def setUp(self):
        self.testStudent1 = Student('Tommy', 'May', 'A01086435', True, ['90'])
        self.testStudent2 = Student('Another', 'Person', 'A01086436', True, [])

    @patch('builtins.input', side_effect=['A01086435', '90', 'done'])
    def test_edit_student_grades(self, mock_input):
        with open('students.txt', 'w') as f_obj:
            f_obj.write('Tommy May A01086435 True 90')
        students_list = [self.testStudent1]
        self.assertTrue(edit_student_grades(students_list))
        os.remove('students.txt')

    @patch('builtins.input', side_effect=['A01034rf34435'])
    def test_invalid_student_number(self, mock_input):
        with open('students.txt', 'w') as f_obj:
            f_obj.write('Tommy May A01086435 True 90')
        students_list = [self.testStudent1]
        self.assertFalse(edit_student_grades(students_list))
        os.remove('students.txt')

    @patch('builtins.input', side_effect=['A01086433'])
    def test_student_not_in_file(self, mock_input):
        with open('students.txt', 'w') as f_obj:
            f_obj.write('Tommy May A01086435 True 90')
        students_list = [self.testStudent1]
        self.assertFalse(edit_student_grades(students_list))
        os.remove('students.txt')
