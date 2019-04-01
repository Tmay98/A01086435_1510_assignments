from unittest import TestCase
from Student_Read import file_read
import os


class TestFile_read(TestCase):

    def test_file_read(self):
        with open('students.txt', 'w') as f_obj:
            f_obj.write('student one A01086435 True 90 95\nstudent two A01086436 True 82 90\n')
        actual_result = file_read()
        expected_result = ['student one A01086435 True 90 95\n', 'student two A01086436 True 82 90\n']
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
