"""Module for updating student info in students.txt"""

# Tommy May
# A01086435

import Student


def edit_student_grades():
    """Asks for student number to add grades to and if the student exists allows user to add grades.

    POSTCONDITION: if student is found asks user for grades and adds them all to student
    RETURN: True if student is on file, False otherwise
    """
    student_number = input('Enter the student number of the student to add grades to\n')
    try:
        # checks if user input was a valid student number
        student_number = Student.check_valid_student_number(student_number)
        # looks for student in file, if it exists adds grades to them
        student_in_file = check_if_student_in_file(student_number)
    except ValueError as e:
        print(e)
        return False
    except FileNotFoundError:
        print('File students.txt does not exist')
        return False
    else:
        return student_in_file


def check_if_student_in_file(student_number):
    """Checks if student number exists in students.txt

    PARAM: student_number a string
    PRECONDITION: student_number must be a correctly formatted student_number
    POSTCONDITION: executes find_student if student exists
    RETURN: True if student exists, false otherwise
    """
    with open("students.txt", "r+") as f_obj:
        lines = f_obj.readlines()
        f_obj.seek(0)
        # checks if specified student is in students.txt
        if student_number in str(lines):
            # goes through lines 1 by 1 writing all students and adding grades to the specified student
            find_student(f_obj, lines, student_number)
            return True
        print('student with that student number is not in the file')
        return False


def find_student(f_obj, lines, student_number):
    """ Writes all lines to file and asks user for grades when the specified student is found

    PARAM: f_obj a file object
    PRECONDITION: f_obj contains lines of student info
    PARAM: lines a list of all the students in students.txt
    PRECONDITION: lines must be a list of correctly formatted students
    PARAM: student_number a string
    PRECONDITION: student_number must be a correctly formatted student number
    POSTCONDITION: the specified student has all grades added in students.txt
    """
    for line in lines:
        if student_number not in str(line):
            f_obj.write(line)
        else:
            add_grades_to_student(f_obj, line)
    f_obj.truncate()


def add_grades_to_student(f_obj, line: str):
    """asks user to add new grades to student

    PARAM: f_obj a file object
    PRECONDITION: f_obj must be a file object
    PARAM: line is a string
    PRECONDITION: line is a correctly formatted students info
    POSTCONDITION: asks for grades to add to the student and writes them to students.txt
    """
    # writes the student to the file excluding the new line character
    f_obj.write(line[:-1])
    while True:
        try:
            # converts grade input to int
            grade = int(input('Enter a grade to add to student type anything else to stop adding\n').strip())
        except ValueError:
            print('non integer grade entered, exiting edit\n')
            break
        # checks if grade is above 100 or below 0. exits loop and prints error message if it is
        if grade < 0 or grade > 100:
            print('You entered a grade below 0 or above 100, exiting edit\n')
            break
        # writes the grade to students.txt if no errors
        else:
            f_obj.write(" " + str(grade))
    # writes the new line character
    f_obj.write('\n')
    print('All valid grades were added to the student')
