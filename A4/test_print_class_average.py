from unittest import TestCase
from Student_Read import print_class_average
from unittest.mock import patch
import io
from Student import Student


class TestPrint_class_average(TestCase):

    def setUp(self):
        self.testStudent1 = Student('Tommy', 'May', 'A01086435', True, ['90', '80', '70'])
        self.testStudent2 = Student('Another', 'Person', 'A01086436', True, ['100', '60'])
        self.testStudent3 = Student('person', 'three', 'A01086437', True, [])
        self.testStudent4 = Student('person', 'four', 'A01086438', True, [])
        self.testStudent5 = Student('person', 'five', 'A01086439', True, [])

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_class_average(self, mock_output):
        students_list = [self.testStudent1, self.testStudent2]
        print_class_average(students_list)
        actual_output = mock_output.getvalue()
        expected_output = 'the class average is: 80.00%\n\n'
        self.assertEqual(actual_output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_student_with_no_grades_not_added_to_average(self, mock_output):
        students_list = [self.testStudent1, self.testStudent2, self.testStudent3]
        print_class_average(students_list)
        actual_output = mock_output.getvalue()
        expected_output = 'the class average is: 80.00%\n\n'
        self.assertEqual(actual_output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_empty_students_list(self, mock_output):
        students_list = []
        print_class_average(students_list)
        actual_output = mock_output.getvalue()
        expected_output = 'No students in file\n'
        self.assertEqual(actual_output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_all_students_without_grades(self, mock_output):
        students_list = [self.testStudent3, self.testStudent4, self.testStudent5]
        print_class_average(students_list)
        actual_output = mock_output.getvalue()
        expected_output = 'No students with grades found\n'
        self.assertEqual(actual_output, expected_output)
