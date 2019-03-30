""" student class module"""

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
        if not first_name.isalpha():
            raise ValueError("You entered an incorrect first name")
        else:
            self.first_name = first_name
        if not last_name.isalpha():
            raise ValueError("You entered an incorrect last name")
        else:
            self.last_name = last_name
        if not student_number[0] == 'A' or not student_number[1:].isnumeric() or not len(student_number) == 9:
            raise ValueError("You entered an incorrect student number")
        else:
            self.student_number = student_number
        if not type(status) == bool:
            raise ValueError("You did not enter a correct status")
        else:
            self.status = status
        for grade in grades:
            grade = int(grade)
            if grade < 0 or grade > 100:
                raise ValueError("You did not enter correct grades")
        self.grades = grades

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


def main():
    pass


if __name__ == "__main__":
    main()
