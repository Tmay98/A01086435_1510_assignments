from unittest import TestCase
from Student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.testStudent1 = Student('Tommy', 'May', 'A01086435', True, [90])
        self.testStudent2 = Student('Tommy', 'May', 'A01086435', True, [])

    def test_get_first_name(self):
        expected_first_name = 'Tommy'
        actual_first_name = self.testStudent1.get_first_name()
        self.assertEqual(expected_first_name, actual_first_name)

    def test_get_last_name(self):
        expected_last_name = 'May'
        actual_last_name = self.testStudent1.get_last_name()
        self.assertEqual(expected_last_name, actual_last_name)

    def test_get_student_number(self):
        expected_student_number = 'A01086435'
        actual_student_number = self.testStudent1.get_student_number()
        self.assertEqual(expected_student_number, actual_student_number)

    def test_get_status(self):
        expected_status = True
        actual_status = self.testStudent1.get_status()
        self.assertEqual(expected_status, actual_status)

    def test_get_grades(self):
        expected_grades = [90]
        actual_grades = self.testStudent1.get_grades()
        self.assertEqual(expected_grades, actual_grades)

    def test_get_grades_with_empty_list_of_grades(self):
        expected_grades = []
        actual_grades = self.testStudent2.get_grades()
        self.assertEqual(expected_grades, actual_grades)

    def test_incorrect_first_name(self):
        with self.assertRaises(ValueError):
            new_student = Student('342s[,d', 'name', 'A01275843', True, [])

    def test_incorrect_last_name(self):
        with self.assertRaises(ValueError):
            new_student = Student('name', '[erg5g]i', 'A01275843', True, [])

    def test_student_number_too_short(self):
        with self.assertRaises(ValueError):
            new_student = Student('name', 'name', 'A01274', True, [])

    def test_student_number_too_long(self):
        with self.assertRaises(ValueError):
            new_student = Student('name', 'name', 'A0123434523274', True, [])

    def test_student_number_doesnt_start_with_A(self):
        with self.assertRaises(ValueError):
            new_student = Student('name', 'name', 'B01086348', True, [])

    def test_grade_not_int(self):
        with self.assertRaises(ValueError):
            new_student = Student('name', 'name', 'A01086435', True, ['abc'])

    def test_grade_over_100(self):
        with self.assertRaises(ValueError):
            new_student = Student('name', 'name', 'A01086435', True, ['102'])

    def test_grade_under_0(self):
        with self.assertRaises(ValueError):
            new_student = Student('name', 'name', 'A01086435', True, ['-5'])

    def test_grade_equals_100(self):
        try:
            new_student = Student('name', 'name', 'A01086435', True, ['100'])
        except ValueError:
            self.fail("Student constructor raised a ValueError")

    def test_grade_equals_0(self):
        try:
            new_student = Student('name', 'name', 'A01086435', True, ['0'])
        except ValueError:
            self.fail("Student constructor raised a ValueError")
