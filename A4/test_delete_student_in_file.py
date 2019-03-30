from unittest import TestCase
from Student_Record import delete_student_in_file
from Student import Student


class TestDelete_student_in_file(TestCase):

    def test_delete_student_in_file(self):
        delete_student_number = 'A01086436'
        open('students.txt', 'w').close()
        with open('students.txt', 'r+') as f_obj:
            f_obj.write('Tommy May A01086435 True\nAnother Student A01086436 False\n')
            f_obj.seek(0)
            lines = f_obj.readlines()
            f_obj.seek(0)
            delete_student_in_file(f_obj, lines, delete_student_number)
        with open('students.txt') as f_obj:
            actual_output = f_obj.read()
        expected_output = 'Tommy May A01086435 True\n'
        self.assertEqual(actual_output, expected_output)

