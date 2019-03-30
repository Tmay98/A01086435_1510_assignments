"""Module with functions for dealing with the student record file"""

# Tommy May
# A01086435

import Student


def convert_to_bool(status: str) -> bool:
    """converts a string to a bool

    PARAM: status a string
    PRECONDITION: status must be a string
    POSTCONDITION: status is converted to a bool
    RETURN: the converted bool value
    """
    status = status.capitalize()
    if status == 'True':
        return True
    elif status == 'False':
        return False
    else:
        raise ValueError('You entered an incorrect status')


def add_student():
    """Creates a new student object and writes it to a file

    POSTCONDITION: if no errors are found the new student object is added to students.txt
    """
    # takes student info input and splits it into a list
    student_info = input('Enter the information for the new student in format:\n'
                         ' FirstName LastName Student# Standing Grades\n')
    student_info = student_info.split()
    try:
        # converts status to a bool and tries to create a new student object
        student_info[3] = convert_to_bool(student_info[3])
        new_student = Student.Student(student_info[0], student_info[1], student_info[2], student_info[3], student_info[4:])
    except ValueError as e:
        print(e)
    except IndexError:
        print('You did not enter all required fields for the student (FirstName, LastName, Student#, standing)\n')
    else:
        # writes student to students.txt
        file_write(new_student)


def file_write(student: Student):
    """Writes student object to file students.txt

    PARAM: student a student object
    PRECONDITION: student must be a student object
    POSTCONDITION: student is added to file students.txt
    RETURN: True or False depending on if student was successfully added
    """
    with open('students.txt', 'a') as f_obj:
        f_obj.write(str(student))
    print('student added to file')
    return True


def file_delete_student() -> bool:
    """Asks for a student number and deletes the student from file students.txt

    POSTCONDITION: the specified student is deleted from file if it is found
    RETURN: True if student is deleted, False if the student wasnt found
    """
    # Asks for student number to delete
    delete_student_number = input('Enter the student number of the student to be deleted\n')
    with open("students.txt", "r+") as f_obj:
        # reads students.txt into the string lines and checks if the specified student exists
        lines = f_obj.readlines()
        f_obj.seek(0)
        if delete_student_number in str(lines):
            # writes all students to students.txt except the one to delete
            for line in lines:
                if delete_student_number not in str(line):
                    f_obj.write(line)
            f_obj.truncate()
            print('Student deleted successfully')
            return True
        print('student not found')
        return False


def calculate_class_average():
    """Calculates class average and prints it

    POSTCONDITION: if there is 1 or more students calculate the class average and print it
    """
    students_list = file_read()
    # checks if file is empty
    if len(students_list) == 0:
        print('No students in file')
        return
    class_average = 0
    # calculate all students average individually and add them to student_average_list
    student_average_list = calculate_students_average(students_list)
    # calculates and prints all students combined average
    for average in student_average_list:
        class_average += int(average)
    class_average = round(class_average / len(student_average_list), 2)
    print("the class average is: ", class_average, "%\n")


def calculate_students_average(students_list):
    """Calculates all students averages and returns a list of them

    PARAM: students_list is a list
    PRECONDITION: student list must be a list of correctly formatted students
    POSTCONDITION: all students independent averages are calculated and appended to students_average_list
    RETURN: list with all students averages

    """
    student_average_list = []
    # calculates all students individual averages
    for i in range(0, len(students_list)):
        student = students_list[i].split()
        total_grades = 0
        # checks if student has any grades
        if len(student) > 4:
            # calculates the average and appends it to students_average_list
            for j in range(4, len(student)):
                total_grades += int(student[j])
            student_average_list.append(total_grades / (len(student) - 4))
    return student_average_list


def file_read() -> list:
    """Reads students.txt file and returns it as a list

    POSTCONDITION: students.txt is read and added to students_list
    RETURN: list of all students or empty list if no students
    """
    try:
        with open("students.txt") as f_obj:
            students_list = f_obj.readlines()
    except FileNotFoundError:
        print('no students in file\n')
        return []
    else:
        if len(students_list) > 0:
            del students_list[0]
            return students_list
        return []


def print_class_list():
    """prints the class list

    POSTCONDITION: reads students.txt and prints all lines, excluding empty lines
    """
    try:
        with open("students.txt") as f_obj:
            print('Students list:')
            for line in f_obj:
                # if the line isn't empty prints the line
                if line != '\n':
                    print(line)
    except FileNotFoundError:
        print('no students in file\n')


def edit_student_grades():
    """Asks for student number to add grades to and if the student exists allows user to add grades.

    POSTCONDITION: if student is found asks user for grades and adds them all to student
    RETURN: True if student is on file, False otherwise
    """
    student_number = input('Enter the student number of the student to add grades to\n')
    try:
        # checks if user input was a valid student number
        student_number = Student.check_valid_student_number(student_number)
    except ValueError as e:
        print(e)
        return False

    with open("students.txt", "r+") as f_obj:
        lines = f_obj.readlines()
        f_obj.seek(0)
        # checks if specified student is in students.txt
        if student_number in str(lines):
            # goes through lines 1 by 1 writing all students and adding grades to the specified student
            find_student_to_add_grades(f_obj, lines, student_number)
            return True
        print('No students in file')
        return False


def find_student_to_add_grades(f_obj, lines, student_number):
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


def main():
    pass


if __name__ == '__main__':
    main()
