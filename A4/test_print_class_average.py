from unittest import TestCase
from Student_Read import print_class_average
from unittest.mock import patch
import io


class TestCalculate_class_average(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculate_class_average(self, mock_output):
        with open('students.txt', 'w') as f_obj:
            f_obj.write('person three A01086435 True 90 80 70\n')
            f_obj.write('person two A01086436 True 100 60\n')
        print_class_average()
        actual_output = mock_output.getvalue()
        expected_output = 'the class average is: 80.00%\n\n'
        self.assertEqual(actual_output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_student_with_no_grades_not_added_to_average(self, mock_output):
        with open('students.txt', 'w') as f_obj:
            f_obj.write('person three A01086435 True 90 80 70\n')
            f_obj.write('person two A01086436 True 100 60\n')
            f_obj.write('person three A01086437 True\n')
        print_class_average()
        actual_output = mock_output.getvalue()
        expected_output = 'the class average is: 80.00%\n\n'
        self.assertEqual(actual_output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_empty_students_list(self, mock_output):
        with open('students.txt', 'w') as f_obj:
            pass
        print_class_average()
        actual_output = mock_output.getvalue()
        expected_output = 'No students in file\n'
        self.assertEqual(actual_output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_all_students_without_grades(self, mock_output):
        with open('students.txt', 'w') as f_obj:
            f_obj.write('person three A01086435 True\n')
            f_obj.write('person two A01086436 True\n')
            f_obj.write('person three A01086437 True\n')
        print_class_average()
        actual_output = mock_output.getvalue()
        expected_output = 'No students with grades found\n'
        self.assertEqual(actual_output, expected_output)
