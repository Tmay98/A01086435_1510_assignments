from unittest import TestCase
from Student_Read_Write import check_if_student_number_exists
from Student import Student


class TestCheck_if_student_number_exists(TestCase):
    def test_check_if_student_number_exists(self):
        student_number = 'A01086435'
        students_list = [Student('Tommy', 'May', 'A01086435', True, [])]
        with self.assertRaises(ValueError):
            check_if_student_number_exists(student_number, students_list)

    def test_student_number_doesnt_exist_no_error_raised(self):
        student_number = 'A01086436'
        students_list = [Student('Tommy', 'May', 'A01086435', True, [])]
        check_if_student_number_exists(student_number, students_list)
