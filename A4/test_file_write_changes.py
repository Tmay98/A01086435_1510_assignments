from unittest import TestCase
from Student_Updating import file_write_changes
import os
from Student import Student


class TestFile_write_changes(TestCase):

    def setUp(self):
        self.testStudent1 = Student('Person', 'One', 'A01086435', True, ['90'])
        self.testStudent2 = Student('Person', 'Two', 'A01086436', True, ['90', '80'])

    def test_file_write_changes(self):
        students_list = [self.testStudent1, self.testStudent2]
        file_write_changes(students_list)
        with open('students.txt') as f_obj:
            actual_output = f_obj.read()
        expected_output = '\nPerson One A01086435 True 90\nPerson Two A01086436 True 90 80'
        self.assertEqual(actual_output, expected_output)
        os.remove('students.txt')
