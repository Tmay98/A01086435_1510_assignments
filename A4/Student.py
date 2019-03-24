""" student class module"""

# Tommy May
# A01086435


class Student:

    def __init__(self, first_name: str, last_name: str, student_number: str, status: bool, grades: list):
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


def add_student(student_info):
    student_info = student_info.split()
    student_info[3] = bool(student_info[3].upper())
    try:
        new_student = Student(student_info[0], student_info[1], student_info[2], student_info[3], student_info[4:])
    except ValueError:
        print('You did not enter correct info for the new student')
        return
    else:
        file_write(new_student)


def file_write(student):
    try:
        grades = ''
        for grade in student.get_grades():
            grades += grade + ' '
        with open('students.txt', 'a') as f_obj:
            f_obj.write("\n" + student.get_first_name() + " " + student.get_last_name() + " " +
                        student.get_student_number() + " " + str(student.get_status()) +
                        " " + grades)
    except FileNotFoundError:
        return False
    else:
        return True


def file_delete_student(student_number: str) -> bool:
    with open("students.txt", "r+") as f_obj:
        lines = f_obj.readlines()
        f_obj.seek(0)
        if student_number in str(lines):
            for line in lines:
                if student_number not in str(line):
                    f_obj.write(line)
            f_obj.truncate()
            return True
        return False


def calculate_class_average():
    try:
        with open("students.txt") as f_obj:
            students_list = f_obj.readlines()
    except FileNotFoundError:
        print('no students in file')
    else:
        grades = []
        class_average = 0
        for i in range(1, len(students_list)):
            student = students_list[i].split()
            for j in range(4, len(student)):
                grades.append(student[j])
        for grade in grades:
            class_average += int(grade)
        return class_average / (len(students_list) - 1)





def main():
    student1 = 'tom may A01086435 true 50'
    student2 = 'tom may A01086436 true 100'
    student3 = 'tom may A01086437 true 12 21 32'
    student4 = 'tom may A01086438 true 12 21 32'
    add_student(student1)
    add_student(student2)
    print(calculate_class_average())

if __name__ == "__main__":
    main()
