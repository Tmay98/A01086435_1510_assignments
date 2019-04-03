from unittest import TestCase
from Student_Updating import delete_student_in_memory
from Student import Student


class TestDelete_student_in_memory(TestCase):
    def test_delete_student_in_memory(self):
        person_one = Student('Tommy', 'May', 'A01086435', True, [])
        person_two = Student('Random', 'Person', 'A01086436', False, [])
        students_list = [person_one, person_two]
        expected_students_list = [person_one]
        student_number = 'A01086436'
        delete_student_in_memory(students_list, student_number)
        self.assertEqual(students_list, expected_students_list)

    def test_student_number_not_found(self):
        person_one = Student('Tommy', 'May', 'A01086435', True, [])
        person_two = Student('Random', 'Person', 'A01086436', False, [])
        students_list = [person_one, person_two]
        student_number = 'A01086438'
        with self.assertRaises(ValueError):
            delete_student_in_memory(students_list, student_number)
