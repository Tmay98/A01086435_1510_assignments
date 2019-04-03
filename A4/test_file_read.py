from unittest import TestCase
from Student_Read_Write import file_read
import os
from Student import Student


class TestFile_read(TestCase):

    def setUp(self):
        self.testStudent1 = Student('Tommy', 'May', 'A01086435', True, ['90'])
        self.testStudent2 = Student('Another', 'Person', 'A01086436', True, [])

    def test_file_read(self):
        with open('students.txt', 'w') as f_obj:
            f_obj.write(str(self.testStudent1))
            f_obj.write(str(self.testStudent2))
        actual_result = file_read()
        actual_result[0] = str(actual_result[0])
        actual_result[1] = str(actual_result[1])
        expected_result = [str(self.testStudent1), str(self.testStudent2)]
        self.assertEqual(expected_result, actual_result)

    def test_empty_file(self):
        with open('students.txt', 'w') as f_obj:
            pass
        actual_result = file_read()
        expected_result = []
        self.assertEqual(expected_result, actual_result)

    def test_file_doesnt_exist(self):
        try:
            os.remove('students.txt')
        except FileNotFoundError:
            pass
        actual_result = file_read()
        expected_result = []
        self.assertEqual(expected_result, actual_result)
