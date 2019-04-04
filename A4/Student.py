"""student class module"""

# Tommy May
# A01086435


class Student:

    def __init__(self, first_name: str, last_name: str, student_number: str, status: bool, grades: list):
        """ Student class constructor
        :param first_name:
        :param last_name:
        :param student_number:
        :param status:
        :param grades:
        """
        if self.check_valid_name(first_name) and self.check_valid_name(last_name):
            self.first_name = first_name.capitalize()
            self.last_name = last_name.capitalize()
        if self.check_valid_student_number(student_number):
            self.student_number = student_number
        if self.check_valid_grades(grades):
            self.grades = grades
        self.status = status

    def __str__(self):
        return "\n" + self.first_name + " " + self.last_name + " " +\
            self.student_number + " " + str(self.status) +\
            ' ' + ' '.join(self.grades)

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_student_number(self):
        return self.student_number

    def get_status(self):
        return self.status

    def get_grades(self):
        return self.grades

    def get_gpa(self) -> float:
        total_grades = 0
        if len(self.grades) > 0:
            for i in range(0, len(self.grades)):
                total_grades += float(self.grades[i])
            return total_grades / len(self.grades)
        return -1

    def add_grade(self, grade):
        self.grades.append(grade)

    def check_valid_student_number(self, student_number):
        if not student_number[0] == 'A' or not student_number[1:].isnumeric() or not len(student_number) == 9:
            raise ValueError("You entered an incorrect student number")
        else:
            return True

    def check_valid_name(self, name):
        if not name.isalpha():
            raise ValueError("You entered an incorrect name")
        else:
            return True

    def check_valid_grades(self, grades):
        for grade in grades:
            grade = float(grade)
            if grade < 0 or grade > 100:
                raise ValueError("You did not enter correct grades")
        return True


def main():
    pass


if __name__ == "__main__":
    main()
