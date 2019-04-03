from unittest import TestCase
from Student_Updating import find_student
from Student import Student


class TestFind_student(TestCase):
    def test_find_student(self):
        person_one = Student('Tommy', 'May', 'A01086435', True, [])
        person_two = Student('Random', 'Person', 'A01086436', False, [])
        students_list = [person_one, person_two]
        student_number = 'A01086435'
        index = find_student(student_number, students_list)
        self.assertEqual(index, 0)

    def test_student_does_not_exist(self):
        person_one = Student('Tommy', 'May', 'A01086435', True, [])
        person_two = Student('Random', 'Person', 'A01086436', False, [])
        students_list = [person_one, person_two]
        student_number = 'A01086437'
        with self.assertRaises(ValueError):
            index = find_student(student_number, students_list)
