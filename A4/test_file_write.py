from unittest import TestCase
from Student_Creation import file_write
from Student import Student


class TestFile_write(TestCase):

    def setUp(self):
        self.testStudent1 = Student('Tommy', 'May', 'A01086435', True, ['90'])

    def test_file_write(self):
        expected_output = '\nTommy May A01086435 True 90'
        open('students.txt', 'w').close()
        file_write(self.testStudent1)
        with open('students.txt', 'r') as f_obj:
            actual_output = f_obj.read()
        self.assertEqual(expected_output, actual_output)

    def test_file_write_appends(self):
        expected_output = 'stuff\nTommy May A01086435 True 90'
        with open('students.txt', 'w') as f_obj:
            f_obj.write('stuff')
        file_write(self.testStudent1)
        with open('students.txt', 'r') as f_obj:
            actual_output = f_obj.read()
        self.assertEqual(expected_output, actual_output)

