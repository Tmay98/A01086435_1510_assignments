"""student class module"""

# Tommy May
# A01086435


class Student:

    def __init__(self, first_name: str, last_name: str, student_number: str, status: bool, grades: list):
        """ Student class constructor

        PARAM: first_name a string
        PRECONDITION: first_name must be a string containing only letters and isn't empty space
        PARAM: last_name a string
        PRECONDITION: last_name must be a string containing only letters and isn't empty space
        PARAM: student_number: a string
        PRECONDITION: student_number must be a string in format A########
        PARAM: status: a bool
        PRECONDITION: status must be a bool
        PARAM: grades a list
        PRECONDITION: grades is a list of numbers between 0 and 100
        POSTCONDITION: a student object is created
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
        """converts a student object into a string for printing

        RETURN: student object formatted into a string
        """
        return "\n" + self.first_name + " " + self.last_name + " " +\
            self.student_number + " " + str(self.status) +\
            ' ' + ' '.join(self.grades)

    def get_first_name(self):
        """ returns the students first name

        RETURN: students first name
        """
        return self.first_name

    def get_last_name(self):
        """ returns the students last name

        RETURN: students last name
        """
        return self.last_name

    def get_student_number(self):
        """ returns the students student number

        RETURN: students student number
        """
        return self.student_number

    def get_status(self):
        """ returns the students status

        RETURN: students status
        """
        return self.status

    def get_grades(self):
        """ returns list of students grades

        RETURN: a list of students grades
        """
        return self.grades

    def get_gpa(self) -> float:
        """ returns the students gpa as a float

        RETURN: students gpa
        """
        total_grades = 0
        if len(self.grades) > 0:
            for i in range(0, len(self.grades)):
                total_grades += float(self.grades[i])
            return total_grades / len(self.grades)
        return -1

    def add_grade(self, grade):
        """ adds a grade to the students grades list

        PARAM: grade a float
        PRECONDITION: grade is a float
        POSTCONDITION: grade is added to students grades list
        """
        self.grades.append(grade)

    def check_valid_student_number(self, student_number):
        """ checks if a student number is valid

        PARAM: student_number a string
        PRECONDITION: student_number must be a string
        POSTCONDITION: raises ValueError if student number is invalid
        RETURN: True if student number is valid
        """
        if not student_number[0] == 'A' or not student_number[1:].isnumeric() or not len(student_number) == 9:
            raise ValueError("You entered an incorrect student number")
        else:
            return True

    def check_valid_name(self, name):
        """Checks if name is all alphabetical

        PARAM: name a string
        PRECONDITION: name must be a string
        POSTCONDITION: raises ValueError if name is invalid
        RETURN: True if name is valid
        """
        if not name.isalpha():
            raise ValueError("You entered an incorrect name")
        else:
            return True

    def check_valid_grades(self, grades):
        """checks if a list of grades are all valid

        PARAM: grades a list
        PRECONDITION: grades is a list of floats
        POSTCONDITION: Raises ValueError if a grade is incorrect
        RETURN: True if no incorrect grades
        """
        for grade in grades:
            grade = float(grade)
            if grade < 0 or grade > 100:
                raise ValueError("You did not enter correct grades")
        return True


def main():
    pass


if __name__ == "__main__":
    main()
