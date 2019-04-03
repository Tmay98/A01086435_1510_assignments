from unittest import TestCase
from Student_Read_Write import print_class_list
from unittest.mock import patch
import io
import os


class TestPrint_class_list(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_class_list(self, mock_output):
        with open('students.txt', 'w') as f_obj:
            f_obj.write('student one A01086435 True 90 50\nstudent two A01086436 True 80 70')
        print_class_list()
        expected_result = 'Students list:\nstudent one A01086435 True 90 50\n\nstudent two A01086436 True 80 70\n'
        actual_result = mock_output.getvalue()
        self.assertEqual(expected_result, actual_result)
        os.remove('students.txt')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_file_not_found(self, mock_output):
        try:
            os.remove('students.txt')
        except FileNotFoundError:
            pass
        print_class_list()
        expected_result = 'no students in file\n\n'
        actual_result = mock_output.getvalue()
        self.assertEqual(expected_result, actual_result)
